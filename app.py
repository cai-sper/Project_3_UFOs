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
    return(
         "Welcome to Project 3_UFO!<br/><br/>"
        "Available Routes:<br/>"
        "<a href='/api/v1.0/map'>/api/v1.0/map</a><br/>"
        "<a href='/api/v1.0/yearly_comparison'>/api/v1.0/yearly_comparison</a><br/>"
        "<a href='/api/v1.0/monthly_comparison'>/api/v1.0/monthly_comparison</a><br/>"
    )


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