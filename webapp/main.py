# webapp main.py
# Author: Joey Xie
# Data: July 16th 2024

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, WebSocketException
import asyncio
from typing import List

app = FastAPI()

# connection manager requirements:
# 1, store all connections;
# 2, 
class ConnectionManager:

    def __init__(self):
        self.active_connections : List[WebSocket] = []
 
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        if websocket not in self.active_connections:
            self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

# websocket endpoint requirements:
# 1, When a message is received from a client, broadcast this message to all connected clients;
# 2, Each client should send its username upon connection;
# 3, The server should prepend the username to each message before broadcasting it to other clients.
# 4, Simple System communicate with text;
@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    await manager.broadcast(f"{username}")

    try:
        while True:
            message = await websocket.receive_text()
            await manager.broadcast(f"{username}: {message}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)

    except Exception as e:
        print(f"Server crashed for reason: {e}.")