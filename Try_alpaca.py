import json
import io

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
    print (accountinfo.content)

    return


def create_myorders(symbol, qty,side,type, timeinforce, order_class, limitprice,stopprice, stoplimitprice ):

    data = {
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
            "limit_price": limitprice},

        }
    myorders=r.post(orderurl, json=data, headers=headers)

    print(myorders.content)



    return json.loads(myorders.content)



def create_simple_order(symbol,qty,buy,sell):
    from alpaca.trading.client import TradingClient
    from alpaca.trading.requests import MarketOrderRequest
    from alpaca.trading.requests import LimitOrderRequest
    from alpaca.trading.enums import OrderSide, TimeInForce

    trading_client = TradingClient(api_Key, seckey, paper=True)

    market_order_data = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.GTC
    )
    market_order = trading_client.submit_order(
        order_data=market_order_data
    )

    limit_order_data = LimitOrderRequest(
        symbol=symbol,
        limit_price=sell,
        notional=10000,
        side=OrderSide.SELL,
        time_in_force=TimeInForce.GTC
    )

#create_simple_order('LSTR',100,171.00,174)


def getfilteredasset():
    from alpaca.trading.client import TradingClient
    trading_client = TradingClient(api_Key, seckey)
    aapl_asset = trading_client.get_all_assets()

    filtered_list = [num for num in aapl_asset if ((num.exchange == 'NASDAQ') and (num.tradable))]


    import csv
    import yfinance as yf
    from datetime import datetime, timedelta

    dateparam=str(datetime.now())
    fout='Idea1'+dateparam+'.csv'
    end_date_testing = datetime.today() - timedelta(days=10)
    start_date_testing = datetime.today() - timedelta(days=30)
    start_date_pred = datetime.today() - timedelta(days=9)
    end_date_pred = datetime.today() - timedelta(days=8)

    end_date = pd.Timestamp(datetime.today(), tz='America/New_York')
    start_date = pd.Timestamp((datetime.today() - timedelta(days=20)), tz='America/New_York')

    # hist = yf.download('MRNA', start=start_date_testing, end=end_date_testing, interval='1d')
    # daily_pct_change = (hist['High'] / hist['Open'] - 1) * 100
    # monthly_avg_percentage = daily_pct_change.sum() / daily_pct_change.count()
    # monthly_avg_std = daily_pct_change.std()

    # hist_pred=yf.download('MRNA',start=start_date_pred,end=end_date_pred,interval='1d')
    # df_pred=((hist_pred['Open']+monthly_avg_percentage)-hist_pred['High'])
    columns = ['Ticker', 'Mean', 'std', 'minChange']
    df_kpi = pd.DataFrame(columns=columns)
    df_temp = pd.DataFrame()
    df_kpi['PI'] = 0
    df_kpi['ticker'] = 'test'
    listl = []

    listy = []
    count = 0

    for i in filtered_list:
        symbol = i.symbol
        hist = yf.download(symbol, start=start_date, end=end_date, interval='1d')
        daily_pct_change = (hist['High'] / hist['Open'] - 1) * 100
        test_this = daily_pct_change.mean()
        std_pct_change = daily_pct_change.std()
        min_pct_change = daily_pct_change.min()

        df_temp['Ticker'] = [symbol]
        df_temp['Mean'] = [test_this]
        df_temp['std'] = [std_pct_change]
        df_temp['minChange'] = [min_pct_change]

        df_kpi = pd.concat([df_kpi, df_temp])


    return df_kpi.to_csv(fout)


getfilteredasset()

#stock1=['INZY',1.46,1000,5.49]
#stock2=['OPEN',2.9,1000,1.78]
stock1=['ARDS',3.56,1000,0.4]
stock4=['ACRV',1.56,1000,12.94]
stock5=['MULN',3,10000,0.134]
stock6=['PALI',3,1000,2.37]
create_myorders(stock1[0],stock1[2], "buy","market", "gtc", "bracket",round(stock1[3]*stock1[1],2),round( stock1[3]*0.95,2), round( stock1[3]*0.95,2))

#create_myorders(stock2[0], stock2[2], "buy","market", "gtc", "bracket",round(stock2[3]*stock2[1],2), round(stock2[3]*0.9,2), round(stock2[3]*0.9,2))

#create_myorders(stock3[0], stock3[2], "buy","market", "gtc", "bracket",round(stock3[3]*stock3[1],2),stock3[3]*0.9, stock3[3]*0.9)


#create_myorders(stock4[0], stock4[2], "buy","market", "gtc", "bracket",round(stock4[3]*stock4[1],2), round(stock4[3]*0.9,2), round(stock4[3]*0.9,2))

#create_myorders(stock5[0], stock5[2], "buy","market", "gtc", "bracket",round(stock5[3]*stock5[1],2), round(stock5[3]*0.9,2), round(stock5[3]*0.9,2))

#create_myorders(stock6[0], stock6[2], "buy","market", "gtc", "bracket",round(stock6[3]*stock6[1],2), round(stock6[3]*0.9,2), round(stock6[3]*0.9,2))