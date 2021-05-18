#!/usr/bin/env python
# coding: utf-8


#Get Consumer Key and Consumer Secret

# Alpaca API Variables

API_KEY = "PKA5IYVIHVQAEPJRIIG5"
SECRET_KEY = "XriqyWNab4KD8ex7LodlCr1hs7XKGZF0qqXeB9ly" #Check API AND SECRET KEYs to make sure they are accurate

ALP_URL: str = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(ALP_URL)
ORDERS_URL = "{}/v2/orders".format(ALP_URL)
ASSETS_URL = "{}/v2/assets".format(ALP_URL)
POSITIONS_URL = "{}/v2/positions".format(ALP_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}


# Stocktwits API variables
domain = 'statsing.com'
client_id ='e5602262546c8dff'
client_secret = '8fa5bc8d87809ad35a3a562ef15a5ec35b1ece36'
request_token = 'https://api.stocktwits.com/api/2/oauth/token'
authorize_url = 'https://api.stocktwits.com/api/2/oauth/authorize'
redirect_url = 'http://statsing.com/'
access_token = '5a84f31288f623b59883ed12c6c6a24ce67dab7a'


