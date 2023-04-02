import logging
from logging.config import dictConfig
from typing import Annotated

import httpx
from fastapi import FastAPI, File, Form, UploadFile

from coffee_freaks_api_client import Client
from src.configuration import settings
from src.data_client import DataClient
from src.data_service import DataService
from src.data_store import DataStore
from src.logger_config import LogConfig
from src.model import Item, Result

dictConfig(LogConfig().dict())

client = Client(base_url=settings.api_host)
logger = logging.getLogger("dataproxy")
data_client = DataClient(api_client=client, settings=settings)
data_store = DataStore(data_client=data_client)
data_service = DataService(data_store=data_store)
app = FastAPI(debug=settings.debug)


@app.get("/health")
async def health():
    logger.info(f"Fetching healthcheck of {settings.api_host}")
    result = httpx.get(settings.api_host + "/health")
    logger.debug(result)
    return {settings.api_host: result.status_code}


@app.post("/v1/data", response_model=Result)
async def post_data(item: Item) -> Result:
    result = data_service.process_data(item)
    return result


@app.post("/v1/image")
async def post_image(file: Annotated[UploadFile, File()], roaster_id: Annotated[str, Form()],
                     coffee_id: Annotated[str, Form()]):
    return data_client.insert_coffee_image(roaster_id, coffee_id, file)


@app.on_event("shutdown")
def shutdown_event():
    data_client.logout()
