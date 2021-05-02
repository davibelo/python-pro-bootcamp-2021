from dotenv import load_dotenv
import os
import requests

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

SHEET_NAME = "prices"
SHEET_NAME_SINGULAR = "price"


class DataManager:
    def __init__(self):
        self.api_endpoint = "https://api.sheety.co/3955488f8ee023601d308d21b9639dd3/flightDeals/prices"
        self.api_key = os.getenv("SHEETY_APIKEY")
        self.api_headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }

    def get_sheet_data(self):
        response = requests.get(url=self.api_endpoint,
                                headers=self.api_headers)
        response.raise_for_status()
        return response.json()[SHEET_NAME]

    def update_data(self, item_id, item_key, item_value):
        json_body = {SHEET_NAME_SINGULAR: {item_key: item_value}}
        response = requests.put(url=f"{self.api_endpoint}/{item_id}",
                                headers=self.api_headers,
                                json=json_body)
        response.raise_for_status()
