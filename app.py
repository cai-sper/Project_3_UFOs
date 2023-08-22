# Import the dependencies
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
#################################################
# Database Setup
#################################################
client = MongoClient(port=27017)
db = client['ufo_db']
ufo_sightings = db['ufo_sightings']
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to Project 3_UFO!</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #F4F4F4;
            }
            .container {
                margin-top: 100px;
            }
            .route-link {
                display: block;
                margin: 10px;
                font-size: 18px;
                color: #007BFF;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Project 3_UFO!</h1>
            <p>Explore UFO data through various API endpoints:</p>
            <a class="route-link" href="/api/v1.0/map">View UFO Map</a>
            <a class="route-link" href="/api/v1.0/yearly_comparison">Yearly Comparison</a>
            <a class="route-link" href="/api/v1.0/monthly_comparison">Monthly Comparison</a>
        </div>
    </body>
    </html>
    """
# Create a route that returns the data from the MongoDB as JSON
@app.route('/api/v1.0/json_data', methods=['GET'])
def get_ufo_sightings():
    # Query for all results in database
    results = list(db.ufo_sightings.find({}, {'_id': 0}))
    return jsonify(results)
@app.route("/api/v1.0/map")
def map():
    return render_template('map.html')
@app.route("/api/v1.0/yearly_comparison")
def yearly_comparison():
    return render_template('yearly.html')
@app.route("/api/v1.0/monthly_comparison")
def monthly_comparison():
    return render_template('monthly.html')
# Run Flask
if __name__ == '__main__':
    app.run()