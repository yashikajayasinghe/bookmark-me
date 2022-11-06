##How to run Mock App Server
- Change to test folder in a termnal
- run `python .\flaskMockServer.py`
- It will show the status: i.e.: 
* Running on http://127.0.0.1:5000 <Press CTRL+C to quit>
* Restarting with stat
* Debugger is active!
* Debugger PIN: ###-###-###

## How to run Tests Locally

- Pre-requisite
  - open the Api implementation in the location `api\FindCityTrigger\__init__.py`
  - Run the App locally (f5 in VScode or in command line with Azure Core Tools: `func host start`)

### Run tests with Real Downstream Data
- Run the test: Change to `test` directory and run `pytest -v -E e2e`


### Run Tests Locally with Mocked Downstream Data
- Mock App Server should be up and running for this test to pass
- Run the test: Change to `test` directory and run  `pytest -v -E acceptance`

Ref: 
Flask
https://flask.palletsprojects.com/en/2.2.x/api/
https://flask.palletsprojects.com/en/2.2.x/testing/

Pytest Custom Markers
https://docs.pytest.org/en/7.1.x/example/markers.html
