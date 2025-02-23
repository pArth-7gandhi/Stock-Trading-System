from fastapi import APIRouter, WebSocket
import logging
import asyncio

router = APIRouter()
active_connections = []

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logging.info("New WebSocket Connection!")
    active_connections.append(websocket)
    await websocket.send_json({"message": "Welcome to the WebSocket! I am doing fine"})  # Send a test message
    try:
        while True:
            message = await websocket.receive_text()
            print(f"Received from Client: {message}")
            await websocket.send_json({"message": f"You sent: {message}"})
            # await asyncio.sleep(50)
    except Exception as e:
        print(f"WebSocket error: {e}")
        active_connections.remove(websocket)

