import requests
import pandas as pd
from os import environ


apikey=environ["APIKEYENV"]

def get_data(stock):

    company_quote = requests.get(f'https://financialmodelingprep.com/api/v3/quote/{stock}?apikey={apikey}')

    share_price = company_quote.json()

    print(share_price)


get_data("PAGS")


