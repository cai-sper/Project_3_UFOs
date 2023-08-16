# Import the dependencies
from flask import Flask, jsonify
from pymongo import MongoClient

# Flask setup
app = Flask(__name__)

# Configure MongoDB connection
client = MongoClient(port=27017)
db = client['ufo_db']
ufo_sightings = db['ufo_sightings']

# Create a route that returns the data from the MongoDB as JSON
@app.route('/', methods=['GET'])

def get_ufo_sightings():

    # Query for all results in database
    results = list(db.ufo_sightings.find({}, {'_id': 0}))

    return jsonify(results)

# Run Flask
if __name__ == '__main__':
    app.run()