from pydantic import BaseModel, Field
from uuid import UUID


class FoodOption(BaseModel):
    id: UUID
    name: str
    price: float = Field(..., gt=0)
    calories: int = Field(..., gt=0)
    is_healthy: bool


class FoodQuery(BaseModel):
    max_price: float
    prefer_healthy: bool = False