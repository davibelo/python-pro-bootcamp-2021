from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client


# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

# open weather API information
WEATHER_APIKEY = os.getenv("WEATHER_APIKEY")
PARAMETERS = {
    "lat": -8.05428,
    "lon": -34.8813,
    "exclude": "current,minutely,daily",
    "appid": WEATHER_APIKEY
}
WEATHER_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

# SMS API information

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

DEST_NUMBER = "+5581997847711"

# getting weather conditions
response = requests.get(url=WEATHER_API_ENDPOINT, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()

# fetching weather ids for 12h with list comprehension
weather_ids_12h = [
    weather_data["hourly"][i]["weather"][0]["id"] for i in range(12)
]
# print(weather_ids_12h)

# initializing a will rain bool
will_rain = False

# checking if weather condition is rainy
for id in weather_ids_12h:
    if id < 700:
        will_rain = True

# sending sms for rainy conditions
if will_rain:
    print("sending SMS...")
    message = client.messages.create(
        body="Is is going to rain today, bring a umbrella!",
        from_="+13025664228",
        to=DEST_NUMBER
    )

    print(f"message sid: {message.sid}")
else:
    print("there is not going to rain, no need for SMS")
