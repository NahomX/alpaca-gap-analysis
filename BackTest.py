import json

from datetime import datetime
import pytz

import backtrader as bt

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

import backtrader as bt
import pandas as pd

# Define strategy
class SMACrossOver(bt.Strategy):
    params = dict(
        pfast=30,  # Period for the fast moving average
        pslow=60,  # Period for the slow moving average
    )

    def __init__(self):
        self.sma_fast = bt.indicators.SMA(self.data, period=self.p.pfast)
        self.sma_slow = bt.indicators.SMA(self.data, period=self.p.pslow)
        self.crossover = bt.indicators.CrossOver(self.sma_fast, self.sma_slow)
        self.buy_bracket()

    def next(self):
        if self.crossover > 0:  # If the fast MA crosses above the slow MA
            self.buy()  # Buy

        elif self.crossover < 0:  # If the fast MA crosses below the slow MA
            self.sell()  # Sell

# Load data
import yfinance as yf
from datetime import datetime, timedelta
end_date_testing = datetime.today() - timedelta(days=10)
start_date_testing = datetime.today() - timedelta(days=30)
start_date_pred = datetime.today() - timedelta(days=9)
end_date_pred = datetime.today() - timedelta(days=8)

data = yf.download('AAPL',start=start_date_testing,end=end_date_testing,interval='60m')

data = bt.feeds.PandasData(dataname=data)

# Instantiate Cerebro engine
cerebro = bt.Cerebro()

# Add data feed
cerebro.adddata(data)



# Add strategy
cerebro.addstrategy(SMACrossOver)


# Set initial cash and commission
cerebro.broker.setcash(100000.0)
cerebro.broker.setcommission(commission=0.001)

# Run backtest
cerebro.run()

#Print results
print(f"Final portfolio value: {cerebro.broker.getvalue():,.2f}")
#df['Diff'] = df['Adj Close']-df['OpeningPrice']
    #df['takeProfitprice'] = df['OpeningPrice']*(1+df['minChange'])
    #df['StopLimit'] = df['OpeningPrice']*(0.95)
    #df['SuccessInd']=df['Diff'].apply(lambda  x : 1 if x >=df['takeProfitprice']  else -1 if x<=df['StopLimit'] else 0)
