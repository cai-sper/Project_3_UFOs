// Declare arrays to store data
const latitude = [];
const longitude = [];
const shape = [];
const datetime = [];

// Fetch data and perform operations when data is available
fetch('http://localhost:5000/api/v1.0/json_data')
  .then(response => response.json())
  .then(dataResponse => {
    // Store fetched data in the 'data' variable
    const data = dataResponse;

    // Initialize the Leaflet map
    let myMap = L.map("map", {
      center: [45.52, -122.67],
      zoom: 6,
      // dimensions to fit browser
    });

    // Add a tile layer to the map
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(myMap);

    // Create a marker cluster group
    let markers = L.markerClusterGroup();

    // Loop through the data and add markers
    for (let i = 0; i < data.length; i++) {
      let lat = data[i].latitude;
      let lon = data[i].longitude;

      // Check if latitude and longitude are valid
      if (lat !== undefined && lon !== undefined) {
        markers.addLayer(L.marker([lat, lon]).bindPopup("Alien encounter"));

        // Push data to respective arrays
        latitude.push(lat);
        longitude.push(lon);
        shape.push(data[i].shape);
        datetime.push(data[i].datetime);
      }
    }

    // Add the marker cluster group to the map
    myMap.addLayer(markers);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
    
  
