import string
from flask import Flask, make_response
from flask import jsonify
import json

app = Flask("zippo")

@app.route('/nz/6035', methods = ['GET'])
def zippo_app():    

    response_body = {
        "post code": "6035",
        "country": "New Zealand",
        "country abbreviation": "NZ",
        "places": [
            {
            "place name": "Khandallah",
            "longitude": "174.7942",
            "state": "",
            "state abbreviation": "",
            "latitude": "-41.2466"
            }
        ]
    }
    return jsonify(response_body)
    
app.run(host='127.0.0.1', port=5000, debug=True)