from dotenv import load_dotenv
import os
import requests
import json

REL_PATH = f"{os.path.dirname(__file__)}/"
load_dotenv(dotenv_path=f"{REL_PATH}.env")
APIKEY = os.getenv("APIKEY")

PARAMETERS = {
    "lat": -8.05428,
    "lon": -34.8813,
    "exclude": "current,minutely,daily",
    "appid": APIKEY
}

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url=API_ENDPOINT, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()

weather_ids_12h = [weather_data["hourly"][i]["weather"][0]["id"] for i in range(12)]
print(weather_ids_12h)


# writing to a json file to help visualize data
with open(f"{REL_PATH}weather.json", mode="w", encoding="utf-8") as file:
    json.dump(weather_data, file, ensure_ascii=False, indent=4)
