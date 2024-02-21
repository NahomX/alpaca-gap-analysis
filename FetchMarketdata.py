from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

import alpaca_trade_api_fixed as tradeapi

api_Key="PKHVZCSFHTW35MTCNZ48"
seckey ="HOeLWN6Na9fhsfChBNsi72mPwX2WUnO5HxIcfKQ9"
endpoint = "https://paper-api.alpaca.markets"

import requests as r,json
import math as m
accurl="{}/v2/account".format(endpoint)

orderurl="{}/v2/orders".format(endpoint)

asseturl="{}/v2/assets".format(endpoint)

headers={'APCA-API-KEY-ID':api_Key,'APCA-API-SECRET-KEY':seckey}


from alpaca.trading.client import TradingClient
trading_client = TradingClient(api_Key, seckey)
aapl_asset = trading_client.get_all_assets()

import csv
import yfinance as yf
from datetime import datetime, timedelta
end_date_testing = datetime.today()
start_date_testing = datetime.today() - timedelta(days=30)


hist = yf.download('MRNA', start=start_date_testing, end=end_date_testing, interval='1d')
daily_pct_change = (hist['High'] / hist['Open'] - 1) * 100

monthly_avg_percentage = daily_pct_change.sum() / daily_pct_change.count()
monthly_min = (hist['Low']).mean()
monthly_low = hist['Low'].min()

current_price = hist['Close'][-1]
trading_price = hist['Close'][-1]+monthly_avg_percentage
monthly_avg_std = daily_pct_change.std()
confidence_selling_price = monthly_min-1.984*monthly_avg_std/m.sqrt(daily_pct_change.count())
daily_risk = current_price*.95

selling_price = daily_risk
if selling_price < monthly_low:
    selling_price = monthly_low
if selling_price > confidence_selling_price:
    selling_price = confidence_selling_price

print(trading_price,selling_price)

market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=0.023,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )

limit_order_data = LimitOrderRequest(
                    symbol="BTC/USD",
                    limit_price=17000,
                    notional=4000,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.FOK
                   )

# Limit order
limit_order = trading_client.submit_order(
                order_data=limit_order_data
              )
def create_myorders(symbol,type,qty,side,timeinforce,order_class,stopprice,stoplimitprice,limitprice):

    data={
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": timeinforce,
        "order_class": order_class,
        "stop_loss": {
            "stop_price": stopprice,
            "limit_price": stoplimitprice
                },
        "take_profit": {
            "limit_price": limitprice}

            }

    myorders=r.post(orderurl, json=data,headers=headers)

    return json.load(myorders.content)

#my_fristorder=create_myorders('MRNA',"market",1,"buy","gtc","bracket",selling_price,selling_price,trading_price)

