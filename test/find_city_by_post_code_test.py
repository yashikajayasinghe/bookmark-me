import pytest
import requests
import json
import jsonpath

BASE_URL = "http://localhost:7071/"

@pytest.mark.env("acceptance")
def test_successfully_finding_city_details_acceptance():
    path = "find_city_details?country=nz&postcode=6035"
    response = requests.get(url=BASE_URL+path)
    print(response.json)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson,'$.post code')[0] == "6035"
    assert jsonpath.jsonpath(responseJson,'$.places[0].place name')[0] == "Khandallah"

@pytest.mark.env("e2e")
def test_successfully_finding_city_details_e2e():
    path = "find_city_by_post_code?country=nz&postcode=6035"
    response = requests.get(url=BASE_URL+path)
    print(response.json)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson,'$.post code')[0] == "6035"
    assert jsonpath.jsonpath(responseJson,'$.places[0].place name')[0] == "Khandallah"