import json
import requests

def api_function():
    """
    - function will determine real time 
    currency exchange rate from USD to SGD
    - no parameter required
    """
    
    # please 
    api_key = ""
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
    
    # use get method from requests on the api url
    response = requests.get(url)
    # use json method from requests to get data
    forex = response.json()
    # extract conversion value from the key: "Realtime Currency Exchange Rate""5. Exchange Rate"
    return float(forex["Realtime Currency Exchange Rate"]["5. Exchange Rate"])   

api_function()
