from fastapi import APIRouter, WebSocket, HTTPException
from typing import List
from app.schemas.order import Order
from app.models.database import get_db_connection

router = APIRouter()

@router.post("/orders")
async def create_order(order: Order):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (symbol, price, quantity, order_type, limit_price, status, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (order.symbol, order.price, order.quantity, order.order_type, order.limit_price, order.status, order.timestamp.isoformat()))
    conn.commit()
    order_id = cursor.lastrowid
    conn.close()
    return {"id": order_id, **order.dict()}

@router.get("/orders", response_model=List[Order])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT symbol, price, quantity, order_type, limit_price, status, timestamp FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return [dict(order) for order in orders]
