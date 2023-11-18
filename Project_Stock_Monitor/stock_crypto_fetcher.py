import requests
import json
from hidden_items import stock_monitor1

# Global variables
API_key = stock_monitor1.coingecko_API_key

# Path for generatign json file
# json_file = open("coin_gecko_api.json", "w")
# pretty_contents= json.dumps(contents, indent=2)
# json_file.write(pretty_contents)

# Gets the price of coin based of name -> uses coingecko
def get_coin_price(coin_name, currency):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_name}"
    req = requests.get(url)
    contents = req.json()
    price = f"Price of {coin_name.capitalize()} in {currency.upper()}:  ${contents['market_data']['current_price'][currency.lower()]}"
    return price

def get_coin_symbol(coin_name):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_name}"
    req = requests.get(url)
    contents = req.json()
    symbol = f"Symbol of {coin_name.capitalize()} is:  {(str(contents['symbol'])).upper()}"
    return symbol

def get_coin_symbol(coin_name):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_name}"
    req = requests.get(url)
    contents = req.json()
    symbol = f"Symbol of {coin_name.capitalize()} is:  {(str(contents['symbol'])).upper()}"
    return symbol



if __name__ == "__main__":
    # get_coin_price(coin_name="ethereum")
    get_coin_price(coin_name="ethereum", currency='USD')
    