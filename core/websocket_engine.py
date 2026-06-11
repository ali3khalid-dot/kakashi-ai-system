import asyncio
import websockets
import json

BINANCE_WS = "wss://stream.binance.com:9443/ws"


async def connect():

    stream = "btcusdt@kline_1m"
    url = f"{BINANCE_WS}/{stream}"

    async with websockets.connect(url) as ws:
        print("✅ WebSocket Connected")

        while True:
            data = await ws.recv()
            msg = json.loads(data)

            if "k" in msg:
                kline = msg["k"]

                if kline["x"]:  # candle closed
                    print("Price:", kline["c"])
