from dotenv import load_dotenv
import os
import requests

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

API_ENDPOINT = "https://api.sheety.co/3955488f8ee023601d308d21b9639dd3/flightDeals/prices"
API_KEY = os.getenv("SHEETY_APIKEY")
API_HEADERS = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

class DataManager:
    def __init__(self) -> None:
        pass
    def get_sheet_data(self):
        response = requests.get(url=API_ENDPOINT, headers=API_HEADERS)
        response.raise_for_status()
        return response.json()["prices"]
    def update_data(self, item_id, item_info):        
        json_body = {"price":{"iataCode":item_info}}
        print(json_body)
        response = requests.put(url=f"{API_ENDPOINT}/{item_id}", headers=API_HEADERS, json=json_body)
        response.raise_for_status()        
