import asyncio
import websockets

from websockets import ServerConnection



async def echo(websockets: ServerConnection):
    async for message in websockets:
        print(f"Получено сообщение {message}")
        response = f"Сервер получил {message}"
        for _ in range(5):
            await websockets.send(response)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())