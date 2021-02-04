import requests


r = requests.get("https://binance.com")
print(r.status_code)
print(r.ok)
