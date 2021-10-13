# coding=utf-8
import asyncio
import websockets
import time

from conn import ConnectionTest
import config
import sys
# import codecs
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

instr_format = "找到仪器 "

ct = ConnectionTest()

async def echo(websocket, path):
    async for message in websocket:
        message = "I got your message: {}".format(message)
        await websocket.send(message)

        while True:
            instr = ct.connection_test(config.test_instr_name)
            res = instr_format + str(instr)
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            time.sleep(1)
            if str(t).endswith("0"):
                await websocket.send(t)
                await websocket.send(res)
                # break

if __name__ == "__main__":
    port = 8765
    print("listening...",port)
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(echo, '0.0.0.0', port))
    asyncio.get_event_loop().run_forever()
