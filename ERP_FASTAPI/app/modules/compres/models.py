from pydantic import BaseModel
from typing import Optional

class Purchase(BaseModel):
    id: Optional[int] = None
    product_name: str
    quantity: int
    price_per_unit: float
    total_price: float

class PurchaseCreate(BaseModel):
    product_name: str
    quantity: int
    price_per_unit: float

class PurchaseUpdate(BaseModel):
    product_name: Optional[str] = None
    quantity: Optional[int] = None
    price_per_unit: Optional[float] = None