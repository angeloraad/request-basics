import requests
# API key (Alpha vantage)
key = "1IV1RA88K6DU32X0"

#API end point 
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey={key}"


s = requests.session()

#GET request using the session
r = s.get(url)

data = r.json()
print(data)