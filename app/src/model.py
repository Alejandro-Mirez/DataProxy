from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):
    title: str
    roasting_date: Optional[str]
    tags: List[str]
    description: str
    details: dict

class Result(BaseModel):
    roaster_id: str
    coffee_id: str