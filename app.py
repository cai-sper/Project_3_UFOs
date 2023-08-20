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
    return(
         "Welcome to Project 3_UFO!<br/><br/>"
        "Available Routes:<br/>"
        "<a href='/api/v1.0/json_data'>/api/v1.0/json_data</a><br/>"
        "<a href='/api/v1.0/yearly_comparison'>/api/v1.0/yearly_comparison</a><br/>"
        # "<a href='/api/v1.0/monthly_comparison'>/api/v1.0/monthly_comparison</a><br/>"
    )

# Create a route that returns the data from the MongoDB as JSON
@app.route('/api/v1.0/json_data', methods=['GET'])
def get_ufo_sightings():

    # Query for all results in database
    results = list(db.ufo_sightings.find({}, {'_id': 0}))

    return jsonify(results)

# a route where we will display a welcome message via an HTML template
@app.route("/api/v1.0/yearly_comparison")
def yearly_comparison():
    return render_template('yearly.html')

# a route where we will display a welcome message via an HTML template
@app.route("/api/v1.0/map")
def yearly_comparison():
    return render_template('map.html')

# Run Flask
if __name__ == '__main__':
    app.run()