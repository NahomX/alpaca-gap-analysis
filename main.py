import alpaca_trade_api_fixed as tradeapi

api=tradeapi.REST('PKHVZCSFHTW35MTCNZ48','HOeLWN6Na9fhsfChBNsi72mPwX2WUnO5HxIcfKQ9',base_url='https://paper-api.alpaca.markets',api_version='v2')

account=api.get_account()

import yfinance as yf
import datetime as dt

import pandas as pd

import yfinance as yf
from datetime import datetime, timedelta

import pandas as pd
# Define the list of tickers to check
tickers_list = ['MRNA','ETSY','DVN','ENPH','PENN',  'TSLA','GRTS','BTCS','UNCY','KBAL']

nasdaq_tickers = yf.Tickers().tickers

# Define the time range to check (past 1 month)
end_date = datetime.today()
start_date = end_date - timedelta(days=30)
count=0
# Check if each ticker has increased by at least 10% each day from its opening price in the past month
for ticker in nasdaq_tickers:
    # Get the historical price data for the ticker
    hist = yf.download(ticker, start=start_date, end=end_date, interval='1d')

    # Calculate the daily percentage change from the opening price
    daily_pct_change = (hist['High'] / hist['Open'] - 1) * 100



    # Check if the ticker has increased by at least 10% each day


    if (daily_pct_change >= .7).all():


        print(f"{ticker} has increased by at least 5% each day from its opening price in the past month")
    else:
        print(f"{ticker} has NOT increased by at least 5% each day from its opening price in the past month")

