import requests

base_url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":"MSFT","datatype":"json","output_size":"compact"}

api_key="4e60c1376cmsh7e136f3b1ff8c60p1ab690jsn5221a06af72a"


headers = {
	"X-RapidAPI-Key": "4e60c1376cmsh7e136f3b1ff8c60p1ab690jsn5221a06af72a",
	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

#response = requests.request("GET", base_url, headers=headers, params=querystring)

#print(response.text)

ma_filter = '50day > 200day'

# Construct the API request URL
params = {
    'function': 'SCREEN_ALL_INDIAN_STOCKS',
    'apikey': api_key,
    'size': 'full',
    'ma': ma_filter
}
url = f'{base_url}?{"&".join(f"{key}={value}" for key, value in params.items())}'

# Send the API request and extract the tickers
response = requests.get(url)
data = response.json()
print(data)

#print(tickers)