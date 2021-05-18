#!/usr/bin/env python
# coding: utf-8

# Write functions for connecting to the alpaca api and making orders


from requests import Response
import requests, json

from stocktwits_secrets import *


def get_account_metadata():
    r: Response = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

#Create function that make a requests and formats the text response in a json object format to be parsed
def get_requests(url):
    #Return json object of messages
    response = requests.get(url)
    response1 = json.loads(response.text)
    
    return response1

def make_order(symbol, qty, side, type, time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }
    r: Response = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(r.content)

def get_buying_power():
    """
        Parameters: Account_URL
        Returns: Buying power from account
    
    """
    return get_account_metadata()['regt_buying_power']

def get_positions():
    r: Response = requests.get(POSITIONS_URL, headers=HEADERS)
    return json.loads(r.content)

def get_asset_price():
    r: Response = requests.get(ASSETS_URL, headers=HEADERS)
    
    return json.loads(r.text)