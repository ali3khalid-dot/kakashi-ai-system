import requests
import time

def get_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    res = requests.get(url).json()
    return res["price"]

print("🔥 Kakashi AI Started 🔥")

while True:
    try:
        price = get_price()
        print("Price:", price)
        time.sleep(5)
    except Exception as e:
        print("Error:", e)
