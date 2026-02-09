from pydantic import BaseModel

# create an object schema corresponding to each table in the database

class ItemsBase(BaseModel):
    item_id: int
    name: str
    dining_hall_id: int
    calories: int
    protein: int
    carbs: int
    fats: int