import asyncio
import websockets
import json

BINANCE_WS = "wss://stream.binance.com:9443/ws"


async def connect():

    stream = "btcusdt@kline_1m"
    url = f"{BINANCE_WS}/{stream}"

    while True:
        try:
            async with websockets.connect(
                url,
                ping_interval=20,
                ping_timeout=20
            ) as ws:

                print("✅ WebSocket Connected")

                while True:
                    data = await ws.recv()
                    msg = json.loads(data)

                    if "k" in msg:
                        kline = msg["k"]

                        if kline["x"]:
                            print("Price:", kline["c"])

        except Exception as e:
            print("❌ Connection Error:", e)
            print("🔄 Reconnecting in 5 seconds...")
            await asyncio.sleep(5)
