import requests
import sys


try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    bitcoin_price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    p = bitcoin_price.json()
    price = p["bpi"]["USD"]
    amount = float(price["rate_float"]) * float(sys.argv[1])
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit("Command-line argument is not a number")
