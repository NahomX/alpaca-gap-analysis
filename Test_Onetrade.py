import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf

testingdate=pd.Timestamp((datetime.today() - timedelta(days=3)), tz='America/New_York')

def fetch_filter(testingdate,interval):

    start_date = testingdate-timedelta(days=interval)
    end_date = testingdate
    from alpaca.trading.client import TradingClient

    api_Key = "PKHVZCSFHTW35MTCNZ48"
    seckey = "HOeLWN6Na9fhsfChBNsi72mPwX2WUnO5HxIcfKQ9"
    endpoint = "https://paper-api.alpaca.markets"

    trading_client = TradingClient(api_Key, seckey)
    asset = trading_client.get_all_assets()
    filtered_list = [num for num in asset if ((num.exchange == 'NASDAQ') & (num.tradable)&(num.symbol=='LSTR'))]
    columns = ['Ticker', 'Mean', 'std', 'minChange']
    df_kpi = pd.DataFrame(columns=columns)
    df_temp = pd.DataFrame()
    df_kpi['PI'] = 0
    df_kpi['ticker'] = 'test'

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

    df_final = df_kpi[(df_kpi['minChange']>0.7) & (df_kpi['std']<1.2)]

    return df_final

data=fetch_filter(testingdate,3)

def setLimitOrders(data):

    #data['OpeningPrice']=  yf.Ticker(i).history(start=testingdate+timedelta(days=1),end=testingdate+timedelta(days=1))
    #data['OpeningPrice']=data['Ticker'].apply(lambda X : yf.Ticker(i).history(start=testingdate+timedelta(days=1),end=testingdate+timedelta(days=1)))
    tradedate=testingdate+timedelta(days=1)
    #data['OpeningPrice']=data['Ticker'].apply(lambda x:yf.Ticker(x).history(start=tradedate,end=tradedate)['Open'][0])
    data['TradeDay'] = tradedate
    data['TradeDay'] = data['TradeDay'].dt.date
    list=[]
    list=data['Ticker'].to_list()

    current_marketdata = yf.download(list,start=tradedate-timedelta(days=2),end=tradedate,interval='1m')
    current_marketdata['TradeDay'] = current_marketdata.index.date
    df = pd.merge(current_marketdata,data[['minChange','TradeDay']],on='TradeDay')
    df['Diff'] = df['Adj Close']-df['Open'][0]
    df['takeProfitprice'] = df['Open'][0]*(1+df['minChange']*0.01)
    df['StopLimit'] = df['Open'][0]*(0.95)
    condition =lambda row: 1 if row['takeProfitprice']<row['Adj Close'] else -1 if row['Adj Close'] < row['StopLimit']else 0
    df['SuccessInd'] = df.apply(condition,axis=1)
    return df.to_csv('Test_backtest.csv')

setLimitOrders(data)


def check_sucess(data,sellprice,buyprice):
    for i in data['PercentageChange']:
        if i==2:
            sucess=2
            break;
        elif i==1:
            sucess=1
            break;
    return sucess
