
import logging
import azure.functions as func
from FastAPIApp import app  # Main API application
import httpx
from starlette.background import BackgroundTask
from starlette.responses import StreamingResponse

@app.get("/find_city_details")
async def find_city(country: str, postcode: int):
    ZIPPO_REAL = "http://api.zippopotam.us/"
    ZIPPO_MOCK = "http://127.0.0.1:5000/"    

    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{ZIPPO_MOCK}{country}/{postcode}")
        return resp.json()

@app.get("/find_city_by_post_code")
async def find_city_resp_stream(country: str, postcode: int):

    ZIPPO_REAL = "http://api.zippopotam.us/"
    client = httpx.AsyncClient()    
    req = client.build_request("GET", f"{ZIPPO_REAL}{country}/{postcode}")
    print(req.method)
    r = await client.send(req, stream=True)

    return StreamingResponse(r.aiter_text(), background=BackgroundTask(r.aclose))
 

def main(req: func.HttpRequest, context:func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req)