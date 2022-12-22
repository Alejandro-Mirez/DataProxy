from fastapi import FastAPI
from configuration import settings
from data_client import DataClient
from data_service import DataService
import openapi_client

configuration = openapi_client.Configuration(
    host=settings.api_host
)
api_client = openapi_client.ApiClient(configuration)
data_client = DataClient(api_client=api_client, settings=settings)
data_service = DataService(data_client=data_client)

app = FastAPI()


@app.get("/health")
async def health():
    result = api_client.call_api("/health", "GET")
    return {settings.api_host: result.status}


@app.post("/v1/data")
async def post_data():
    return data_service.process_data()


@app.on_event("shutdown")
def shutdown_event():
    data_client.logout()
    api_client.close()
