## How to run Tests Locally

- Pre-requisite
  - open the Api implementation in the location `api\FindCityTrigger\__init__.py`
  - Run the App locally (f5 in VScode or in command line with Azure Core Tools: `func host start`)

### Run tests with Real Downstream Data
- Run the test: Change to `test` directory and run `pytest -v -E e2e`


### Run Tests with Mocked Downstream Data
- Run the test: Change to `test` directory and run  `pytest -v -E acceptance`

## Ref: 
### Flask
- https://github.com/neilgall/pytest-docker-flask
- https://flask.palletsprojects.com/en/2.2.x/api/
- https://flask.palletsprojects.com/en/2.2.x/testing/

### Pytest Custom Markers
- https://docs.pytest.org/en/7.1.x/example/markers.html
