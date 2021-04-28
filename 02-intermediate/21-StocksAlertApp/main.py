from dotenv import load_dotenv
import os
import requests
import datetime as dt
from twilio.rest import Client

# stock config
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALERT_LIM = 5

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

# stocks prices API config
ALPHAVANTAGE_KEY = os.getenv("ALPHAVANTAGE_KEY")
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"

ALPHAVANTAGE_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": ALPHAVANTAGE_KEY
}

# getting yesterday time data to use on stocks API
today = dt.datetime.utcnow().date() + dt.timedelta(hours=+4)
yesterday = str(today - dt.timedelta(days=1))
before_yesterday = str(today - dt.timedelta(days=2))

# accessing stocks API and getting data
response = requests.get(url=ALPHAVANTAGE_ENDPOINT, params=ALPHAVANTAGE_PARAMS)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
value_1 = float(data[before_yesterday]["4. close"])
value_2 = float(data[yesterday]["4. close"])

# calculating diference of stock price in percent
dif_percent = abs(100*(value_2-value_1)/(value_1))

print(dif_percent)
if dif_percent > 5:
    pass




# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday
# and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces
# for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's
# title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
