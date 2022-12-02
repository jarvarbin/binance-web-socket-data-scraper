import asyncio
from binance.websockets import BinanceSocketManager
from binance.client import Client

async def process_message(msg):
    print(msg)

async def main():
    client = Client("API_KEY", "API_SECRET")
    bm = BinanceSocketManager(client)
    conn_key = bm.start_kline_socket("BNBBTC", process_message, interval=Client.KLINE_INTERVAL_5MINUTE)
    await bm.start()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
