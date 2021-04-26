from dotenv import load_dotenv
import os
import requests
from requests import api
import json

REL_PATH = f"{os.path.dirname(__file__)}/"
load_dotenv(dotenv_path=f"{REL_PATH}.env")
APIKEY = os.getenv("APIKEY")

parameters = {
    "lat": -8.05428,
    "lon": -34.8813,
    "exclude": "minutely",
    "appid": APIKEY
}

api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url=api_endpoint, params=parameters)
data = response.json()
with open(f"{REL_PATH}weather.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    