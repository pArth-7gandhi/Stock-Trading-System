import logging
from fastapi import FastAPI
from app.crud.requests import router
from app.models.database import init_db
from app.routers.websocket import router as ws_router

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
app.include_router(router)
app.include_router(ws_router)  # Include WebSocket router for realtime updates

init_db()

@app.on_event("startup")
async def startup_event():
    logging.info("FastAPI server is starting up!")

@app.on_event("shutdown")
async def shutdown_event():
    logging.info("FastAPI server is shutting down!")