import requests
import re
blockchainUrl = 'https://blockchain.info/ticker'

def buy(currency):
    # Get the request from blockchain
    request = requests.get(blockchainUrl).json()
    request = str(request[currency])
    # Define the variable value
    value = re.search("(?i)(?s)y':(.*?),", request)
    value = value.group(0).replace("y':", '').replace(',', '')
    # Define the variable symbol, as the currency symbol
    symbol = re.search("(?i)(?s)bol':(.*?)}", request)
    symbol = symbol.group(0).replace("bol':", '').replace('}', '').replace("'", '')

    return(symbol + value)