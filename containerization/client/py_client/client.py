import asyncio
import websockets

addr = "192.168.1.102"
loopback = "127.0.0.1"
port = "8765"
conn_address = 'ws://{0}:{1}'.format(addr, port)

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello van!")
        print("< Hello van!")
        while True:
            recv_text = await websocket.recv()
            print("> {}".format(recv_text))


asyncio.get_event_loop().run_until_complete(hello(conn_address))
