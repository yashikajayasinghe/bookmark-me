import json
import jsonpath
import pytest
import requests
from flask import Flask, jsonify
from framework import Service

BASE_FUNCTION_APP_URL = "https://yashikajayasinghe-stunning-funicular-vppxxv7p445hwgw6-7071.preview.app.github.dev/"


@pytest.fixture
def simple_service():
    """
    Provides a simple service running in the pytest process
    """
    app = Flask('simple-service')

    @app.route('/nz/6035')
    def main():
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
    return Service(app, 5000)


@pytest.mark.env("acceptance")
def test_successfully_finding_city_details_acceptance(simple_service):

    with simple_service as service:

        path = "find_city_details?country=nz&postcode=6035"
        response = requests.get(url=BASE_FUNCTION_APP_URL+path)
        responseJson = json.loads(response.text)
        assert response.status_code == 200
        assert jsonpath.jsonpath(responseJson, '$.post code')[0] == "6035"
        assert jsonpath.jsonpath(responseJson, '$.places[0].place name')[
            0] == "Khandallah"


@pytest.mark.env("e2e")
def test_successfully_finding_city_details_e2e():
    path = "find_city_by_post_code?country=nz&postcode=6035"
    response = requests.get(url=BASE_FUNCTION_APP_URL+path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.post code')[0] == "6035"
    assert jsonpath.jsonpath(responseJson, '$.places[0].place name')[0] == "Khandallah"
