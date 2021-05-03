from dotenv import load_dotenv
import os
import requests

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

class DataManager:
    def __init__(self):
        self.prices_api_endpoint = "https://api.sheety.co/3955488f8ee023601d308d21b9639dd3/flightDeals/prices"
        self.email_api_endpoint = "https://api.sheety.co/3955488f8ee023601d308d21b9639dd3/flightDeals/users"
        self.api_key = os.getenv("SHEETY_APIKEY")
        self.api_headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }

    def get_sheet_data(self):
        response = requests.get(url=self.prices_api_endpoint,
                                headers=self.api_headers)
        response.raise_for_status()
        return response.json()["prices"]

    def update_data(self, item_id, item_key, item_value):
        json_body = {"price": {item_key: item_value}}
        response = requests.put(url=f"{self.prices_api_endpoint}/{item_id}",
                                headers=self.api_headers,
                                json=json_body)
        response.raise_for_status()

    def get_emails(self):
        response = requests.get(url=self.email_api_endpoint,
                                headers=self.api_headers)
        response.raise_for_status()
        return response.json()["users"]
