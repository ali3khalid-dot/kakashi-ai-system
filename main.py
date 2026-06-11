import asyncio
from core.websocket_engine import connect

async def main():
    print("🔥 Kakashi AI Started 🔥")
    await connect()

if __name__ == "__main__":
    asyncio.run(main())
