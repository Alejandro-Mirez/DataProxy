from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    title: str
    roasting_date: str
    tags: List[str]
    description: str
    details: dict