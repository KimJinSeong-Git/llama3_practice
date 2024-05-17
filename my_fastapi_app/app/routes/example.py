from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": "Example Item"}

@router.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}
