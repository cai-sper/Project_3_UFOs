# Import the dependencies
from flask import Flask, send_file
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
                background-color: #f4f4f4;
            }
            .container {
                margin-top: 100px;
            }
            .route-link {
                display: block;
                margin: 10px;
                font-size: 18px;
                color: #007bff;
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


@app.route("/api/v1.0/map", methods=['GET'])
def map():
     return send_file('path_to_external_content.html')


@app.route("/api/v1.0/yearly_comparison", methods=['GET'])
def yearly_comparison():
     return send_file('path_to_external_content.html')


@app.route("/api/v1.0/monthly_comparison", methods=['GET'])
def monthly_comparison():
     # Replace 'path_to_external_content.html' with the actual path to your HTML/JavaScript file
     return send_file('path_to_external_content.html')


# Run Flask
if __name__ == '__main__':
    app.run()