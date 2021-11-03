# coding=utf-8
import asyncio
import websockets
import time


async def echo(websocket):
    async for message in websocket:
        message = "I got your message: {}".format(message)
        await websocket.send(message)

        while True:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            time.sleep(1)
            if str(t).endswith("0"):
                await websocket.send(t)
                break

if __name__ == "__main__":
    port = 8765
    print("listening...",port)
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(echo, '0.0.0.0', port))
    asyncio.get_event_loop().run_forever()
