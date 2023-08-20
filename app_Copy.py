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


# @app.route("/api/v1.0/map", methods=['POST'])
# def map():
#     'static/js/logic.js' = request.json
#     print(content)
#     return jsonify(content)
    # return jsonify({'status': 0, 'msg': 'success'})
# return 'static/js/logic.js'

# Create a route that returns the data from the MongoDB as JSON
@app.route('/api/v1.0/json_data', methods=['GET'])
def get_ufo_sightings():

    # Query for all results in database
    results = list(db.ufo_sightings.find({}, {'_id': 0}))

    return jsonify(results)

# a route where we will display a welcome message via an HTML template
@app.route("/api/v1.0/yearly_comparison")
def yearly_comparison():
    return render_template('index.html')



# @app.route("/api/v1.0/yearly_comparison", methods=['GET'])
# def yearly_comparison():
#      return send_file('path_to_external_content.html')


# @app.route("/api/v1.0/monthly_comparison", methods=['GET'])
# def monthly_comparison():
#      # Replace 'path_to_external_content.html' with the actual path to your HTML/JavaScript file
#      return send_file('path_to_external_content.html')


# Run Flask
if __name__ == '__main__':
    app.run()