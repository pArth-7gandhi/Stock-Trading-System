from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str
    limit_price: float | None = None
    status: str = "pending"
    timestamp: datetime = datetime.utcnow()