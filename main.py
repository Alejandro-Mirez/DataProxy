import logging
import httpx
from fastapi import FastAPI

from logging.config import dictConfig
from configuration import settings
from data_client import DataClient
from data_store import DataStore
from data_service import DataService
from coffee_freaks_api_client import Client
from logger_config import LogConfig

dictConfig(LogConfig().dict())

client = Client(base_url=settings.api_host)
logger = logging.getLogger("dataproxy")
data_client = DataClient(api_client=client, settings=settings)
data_store = DataStore(data_client=data_client)
data_service = DataService(data_client=data_client, data_store=data_store)
app = FastAPI(debug=settings.debug)


@app.get("/health")
async def health():
    logger.info(f"Fetching healthcheck of {settings.api_host}")
    result = httpx.get(settings.api_host + "/health")
    logger.debug(result)
    return {settings.api_host: result.status_code}


@app.post("/v1/data")
async def post_data():
    return data_service.process_data()


@app.on_event("shutdown")
def shutdown_event():
    data_client.logout()
