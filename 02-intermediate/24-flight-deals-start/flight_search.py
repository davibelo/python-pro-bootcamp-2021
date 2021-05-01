from dotenv import load_dotenv
import os
import requests

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

# https://tequila.kiwi.com/portal/docs/tequila_api/search_api
API_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = os.getenv("TEQUILA_KIWI_APIKEY")
API_HEADERS = {"apikey": API_KEY}


class FlightSearch:
    def __init__(self):
        pass

    def get_iata_code(self, city_name):
        api_params = {
            "term": city_name,
            "location_types": "city",
            "locale": "pt-BR"
        }
        response = requests.get(url=f"{API_ENDPOINT}/locations/query",
                                headers=API_HEADERS,
                                params=api_params)

        response.raise_for_status()
        return response.json()["locations"][0]["code"]
