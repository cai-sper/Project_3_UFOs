// Fetch data from local server
fetch('http://127.0.0.1:5000/api/v1.0/json_data')
  .then(response => response.json())
  .then(dataResponse => {
    data = dataResponse; // Assign fetched data to the global variable

// Initialized array
const months = [];
const years = [];
  
// For loop to populate arrays
for (let i = 0; i < data.length; i++) {
  row = data[i];
  months.push(row.Month);
  years.push(row.Year);
 } 

const unique_years = [...new Set(years)];

unique_years.sort(function(a, b) {
  return a - b;
});

// Check that the array is unique years in a ascending order to make the dropdown list
console.log(unique_years);

// Populate dropdown with years
const yearSelector = document.getElementById('yearSelector');

unique_years.forEach(year => {
  const option = document.createElement('option');
  option.value = year;
  option.textContent = year;
  yearSelector.appendChild(option);
});


const amount_months = [];

for (const num of months) {
  amount_months[num] = amount_months[num] ? amount_months[num] + 1 : 1;
}
const counted_months = amount_months.slice(1,);
console.log(counted_months);
  

const months_graph = [
  "Jan", "Feb", "Mar",
  "Apr", "May", "Jun",
  "Jul", "Aug", "Sep",
  "Oct", "Nov", "Dec"
];

let trace = {
  x: months_graph,
  y: counted_months,
  type: 'lines'
};

let axes = [trace];

let layout = {
  title: "Monthly Comparison",
  yaxis: {
    title: "Number of sightings",
    range: [Math.min(...counted_months) - 500, Math.max(...counted_months) + 750]
},
 xaxis: {
  title: "Months"
 }
};

const config = {
  responsive: true
};

Plotly.newPlot("plot", axes, layout, config);
})
