import logging
import azure.functions as func
from FastAPIApp import app  # Main API application
import httpx
from starlette.background import BackgroundTask
from starlette.responses import StreamingResponse

# this is a test endpoint that consumes a mocked downstream system
@app.get("/find_city_details")
async def find_city_details_with_mocked_downstream(country: str, postcode: int):
    
    ZIPPO_MOCK = "http://localhost:5000/"       

    with httpx.Client() as client:
        resp = client.get(f"{ZIPPO_MOCK}{country}/{postcode}")
        print(resp.text)
        if(resp.status_code == 200):
            return resp.json()
        else:
            return 'NOT OKAY'

@app.get("/find_city_by_post_code")
async def find_city_resp_stream_live_downstream(country: str, postcode: int):

    ZIPPO_REAL = "http://api.zippopotam.us/"
    client = httpx.AsyncClient()    
    req = client.build_request("GET", f"{ZIPPO_REAL}{country}/{postcode}")
    print(req.method)
    r = await client.send(req, stream=True)

    return StreamingResponse(r.aiter_text(), background=BackgroundTask(r.aclose))

 
@app.get("/find_city_details_async")
async def find_city_details_with_async_client(country: str, postcode: int):
    
    ZIPPO_MOCK = "http://localhost:5000/"    
    
    client = httpx.AsyncClient()    
    req = client.build_request("GET", f"{ZIPPO_MOCK}{country}/{postcode}")
    print(req.method)
    r = await client.send(req, stream=True)

    return StreamingResponse(r.aiter_text(), background=BackgroundTask(r.aclose))

    # async with httpx.AsyncClient() as client:
    #     resp = await client.get(f"{ZIPPO_MOCK}{country}/{postcode}")
    #     return resp.json()

def main(req: func.HttpRequest, context:func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req)