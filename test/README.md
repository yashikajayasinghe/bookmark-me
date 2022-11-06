##How to run Mock App Server
- Change to test folder in a termnal
- run `python .\flaskMockServer.py`
- It will show the status: i.e.: 
* Running on http://127.0.0.1:5000 <Press CTRL+C to quit>
* Restarting with stat
* Debugger is active!
* Debugger PIN: ###-###-###

## How to run Tests with Real Downstream Data

- Pre-requisite
  - open the Api implementation in the location `api\FindCityTrigger\__init__.py`
  - change the Valiable name of GET request ULR to be 'ZIPPO_REAL' as `req = client.build_request("GET", f"{ZIPPO_REAL}{country}/{postcode}")`
  - Run the App locally (f5 in VScode or in command line with Azure Core Tools: `func host start`)

- Run the test: Change to `test` directory and run `pytest find_city_by_post_code_test.py` or `pytest -v .\find_city_real_downstream_test.py`


## How to run Tests with Mock Downstream Data
- Pre-requisite
  - open the Api implementation in the location `api\FindCityTrigger\__init__.py`
  - change the Valiable name of GET request ULR to be 'ZIPPO_MOCK' as `req = client.build_request("GET", f"{ZIPPO_MOCK}{country}/{postcode}")`
  - Run the App locally (f5 in VScode or in command line with Azure Core Tools: `func host start`)

- Run the test: Change to `test` directory and run `pytest find_city_by_post_code_test.py` or `pytest -v .\find_city_real_downstream_test.py`