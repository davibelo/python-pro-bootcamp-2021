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

    def get_flight_prices(self, departure_code, arrival_code, max_stops,
                          date_initial, date_final, nights_min, nights_max,
                          language, price_limit, currency):
        api_params = {
            "fly_from": departure_code,
            "fly_to": arrival_code,
            "max_stopovers": max_stops,
            "date_from": date_initial,
            "date_to": date_final,
            "nights_in_dst_from": nights_min,
            "nights_in_dst_to": nights_max,
            "locale": language,
            "price_to": price_limit,
            "curr": currency
        }
        response = requests.get(url=f"{self.api_endpoint}/v2/search",
                                headers=self.api_headers,
                                params=api_params)
        result = response.json()["data"][0]
        flight_data = FlightData(
            departure_city=result["cityFrom"],
            departure_airport_code=result["flyFrom"],
            arrival_city=result["cityTo"],
            arrival_airport_code=result["flyTo"],
            departure_date=result["local_departure"].split("T")[0],
            arrival_date=result["local_arrival"].split("T")[0],
            price=result["price"])
        return flight_data
