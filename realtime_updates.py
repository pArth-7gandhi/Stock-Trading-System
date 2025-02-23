import websockets
import asyncio

async def connect():
    uri = "ws://127.0.0.1:8000/ws"
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected to WebSocket server")
            await websocket.send("Hello Server, how is your day going?")
            response = await websocket.recv()
            print(f"Server Response: {response}")

            # Keep connection alive for testing
            # await asyncio.sleep(5)
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"WebSocket Error: {e}")

asyncio.run(connect())
