from dotenv import load_dotenv
import os
import requests
from flight_data import FlightData

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

# https://tequila.kiwi.com/portal/docs/tequila_api/search_api

class FlightSearch:
    def __init__(self):
        self.api_endpoint = "https://tequila-api.kiwi.com"
        self.api_key = os.getenv("TEQUILA_KIWI_APIKEY")
        self.api_headers = {"apikey": self.api_key}

    def get_iata_code(self, city_name):
        api_params = {
            "term": city_name,
            "location_types": "city",
            "locale": "pt-BR"
        }
        response = requests.get(url=f"{self.api_endpoint}/locations/query",
                                headers=self.api_headers,
                                params=api_params)

        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def get_flight_prices(self, destiny_airport_code, price_limit) -> dict:
        flight_data = FlightData()
        api_params = {
            "fly_from": flight_data.departure_airport_code,
            "fly_to": destiny_airport_code,
            "max_stopovers": flight_data.max_stopovers,
            "date_from": flight_data.date_initial,
            "date_to": flight_data.date_final,
            "nights_in_dst_from": flight_data.nights_in_dst_from,
            "nights_in_dst_to": flight_data.nights_in_dst_to,
            "locale": flight_data.locale,
            "price_to": price_limit,
            "curr": flight_data.curr
        }
        response = requests.get(url=f"{self.api_endpoint}/v2/search",
                                headers=self.api_headers,
                                params=api_params)
        result = response.json()["data"][0]
        return {
            "depature_city": result["cityFrom"],
            "departure_airport_code": result["flyFrom"],
            "arrival_city_name": result["cityTo"],
            "arrival_airport_code": result["flyTo"],
            "departure_date": result["local_departure"].split("T")[0],
            "arrival_date": result["local_arrival"].split("T")[0],
            "price": result["price"]
        }
