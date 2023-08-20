
// Fetch data from local server
fetch('http://localhost:5000/api/v1.0/json_data')
  .then(response => response.json())
  .then(dataResponse => {
    data = dataResponse; // Assign fetched data to the global variable
    
    // Process data to get unique years
    const uniqueYears = getUniqueYears(data);

    // Populate dropdown with years
    const yearSelector = document.getElementById('yearSelector');
    uniqueYears.forEach(year => {
      const option = document.createElement('option');
      option.value = year;
      option.textContent = year;
      yearSelector.appendChild(option);
    });

    // Add event listener for dropdown change
    yearSelector.addEventListener('change', handleYearSelection);
    
    // Create initial Plotly chart with all years
    createPlotlyVisualization(data);
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });

// Get unique years from data and sort them
function getUniqueYears(data) {
  const years = new Set();
  data.forEach(entry => years.add(entry.Year));
  return Array.from(years).sort((a, b) => a - b);
}

// Handle year selection from dropdown
function handleYearSelection() {
  const selectedYears = Array.from(
    document.querySelectorAll('#yearSelector option:checked')
  ).map(option => option.value);

  // Filter data based on selected years
  const filteredData = data.filter(entry => {
    const year = new Date(entry.datetime).getFullYear().toString();
    return selectedYears.includes(year) || selectedYears.includes('all');
  });

  // Log the filteredData to the console for debugging
  console.log('Filtered Data:', filteredData);

  // Update Plotly chart with filtered data
  createPlotlyVisualization(filteredData);
}

// Create a Plotly bar chart
function createPlotlyVisualization(data) {
  const yearCounts = {};
  data.forEach(entry => {
    const year = entry.Year;
    yearCounts[year] = (yearCounts[year] || 0) + 1;
  });

  const xValues = Object.keys(yearCounts);
  const yValues = Object.values(yearCounts);

  const trace = {
    x: xValues,
    y: yValues,
    type: 'bar'
  };

  const layout = {
    title: 'Encounters Per Year',
    xaxis: {
      title: 'Year',
      tickvals: xValues,
      ticktext: xValues.map(year => year.toString())
    },
    yaxis: {
      title: 'Number of Encounters'
    },
    margin: {
      l: 50,
      r: 50,
      t: 50,
      b: 50
    }
  };

  const config = {
    responsive: true
  };

  Plotly.newPlot('yearlyBar', [trace], layout, config);
}
