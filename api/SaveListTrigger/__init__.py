
import logging
import azure.functions as func
from FastAPIApp import app  # Main API application
import httpx
from starlette.background import BackgroundTask
from starlette.responses import StreamingResponse

@app.get("/find_city_details")
async def find_city(country: str, postcode: int):
        
    client = httpx.AsyncClient()    
    req = client.build_request("GET", f"http://api.zippopotam.us/{country}/{postcode}")
    r = await client.send(req, stream=True)
    return StreamingResponse(r.aiter_text(), background=BackgroundTask(r.aclose))

def main(req: func.HttpRequest, context:func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req)