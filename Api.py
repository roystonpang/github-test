import json
import requests

def api_function():
    api_key = ""
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
    response = requests.get(url)
    forex = response.json()
    return float(forex["Realtime Currency Exchange Rate"]["5. Exchange Rate"])   

api_function()
