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

function filterYear(array, targetYear) {
  return array.filter(item => item.Year === targetYear);
}

const dropdown = document.getElementById("dropdown");

// List of values you want to populate the dropdown with
const values = unique_years;

// Loop through the values and create an option element for each
values.forEach(value => {
  const option = document.createElement("option");
  option.text = value;
  option.value = value; 
  dropdown.appendChild(option);
});

dropdown.addEventListener("change", function() {
  const selectedValue = dropdown.value;
  updateGraph(selectedValue)
});

function countMonths(arr){
const amount_months = [];

for (const num of arr) {
  amount_months[num] = amount_months[num] ? amount_months[num] + 1 : 1;
}
return amount_months
}

const counted_months = countMonths(months).slice(1,);
  
const months_graph = [
  "Jan", "Feb", "Mar",
  "Apr", "May", "Jun",
  "Jul", "Aug", "Sep",
  "Oct", "Nov", "Dec"
];


function updateGraph() {
 const selectedValue = dropdown.value

let data_filtered = [];
data_filtered = filterYear(data, parseInt(selectedValue));

const months_filtered = [];
const years_filtered = [];

// For loop to populate arrays
for (let i = 0; i < data_filtered.length; i++) {
  row = data_filtered[i];
  months_filtered.push(row.Month);
  years_filtered.push(row.Year);
 } 

const counted_months_filtered = countMonths(months_filtered).slice(1,);


 let trace = {
  x: months_graph,
  y: counted_months_filtered,
  type: 'lines'
};

let axes = [trace];

let layout = {
  title: "Monthly Comparison",
 xaxis: {
  title: "Months"
 },
 yaxis: {
  title: "Number of sightings",
  range: [Math.min(...counted_months_filtered) - 500, Math.max(...counted_months_filtered) + 750]
},
};

const config = {
  responsive: true
};

Plotly.newPlot("plot", axes, layout, config);
}

function init() {

let trace = {
  x: months_graph,
  y: countMonths(months).slice(1,),
  type: 'lines'
};

let axes = [trace];

let layout = {
  title: "Monthly Comparison",
 xaxis: {
  title: "Months"
 },
 yaxis: {
  title: "Number of sightings",
  range: [Math.min(...counted_months) - 500, Math.max(...counted_months) + 750]
},
};

const config = {
  responsive: true
};

Plotly.newPlot("plot", axes, layout, config);
}

init();
}
  )
