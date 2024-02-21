import json
import io

import yfinance as yf
from datetime import datetime, timedelta
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest,GetAssetsRequest
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

api_Key = "PKHVZCSFHTW35MTCNZ48"
seckey = "HOeLWN6Na9fhsfChBNsi72mPwX2WUnO5HxIcfKQ9"
endpoint = "https://paper-api.alpaca.markets"

import pandas as pd
import requests as r
import json as j

accurl = "{}/v2/account".format(endpoint)

orderurl = "{}/v2/orders".format(endpoint)

asseturl = "{}/v2/assets".format(endpoint)

headers = {'APCA-API-KEY-ID': api_Key, 'APCA-API-SECRET-KEY': seckey}

def getmy_account():

    accountinfo = r.get(accurl, headers=headers)

    return accountinfo

trading_client = TradingClient(api_Key, seckey)
aapl_asset = trading_client.get_all_assets()

#filtered_list = [num for num in aapl_asset if ((num.exchange == 'NASDAQ') and (num.tradable) and num.symbol=='AAPL')]

sum([round(premium(c, data.s, r=0.05, T=0.13778), 2) for c in data.c])