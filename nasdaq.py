import alpaca_trade_api_fixed as tradeapi

api_Key = "PKHVZCSFHTW35MTCNZ48"
seckey = "HOeLWN6Na9fhsfChBNsi72mPwX2WUnO5HxIcfKQ9"
endpoint = "https://paper-api.alpaca.markets"

api = tradeapi.REST(key_id=api_Key,secret_key=seckey,base_url='https://paper-api.alpaca.markets',api_version='v2')

symbol = 'ICG'
symbol_bars = api.get_barset(symbol, 'minute').df.iloc[0]
symbol_price = symbol_bars[symbol]['close']


