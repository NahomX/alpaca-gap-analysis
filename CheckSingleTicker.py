apikey='gDH95oar2HKA7ZU4oQNa'
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
end_date = pd.Timestamp((datetime.today() - timedelta(days=0)), tz='America/New_York')
start_date = pd.Timestamp((datetime.today() - timedelta(days=1)), tz='America/New_York')
hist = yf.download('AAPL', start=start_date, end=end_date, interval='1d')
df_eda=pd.DataFrame(hist)
stockdata=yf.Ticker('AAPL').history(start=end_date-timedelta(days=1),end=end_date)

#print(df_eda.Open,df_eda.Low.min(),df_eda.High.max(),df_eda.High.max()/df_eda.Open[0])
print(stockdata['High'])

#data = yf.download('AAPL',start=start_date,end=end_date,interval='60m')




