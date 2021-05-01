# This file will need to use the this classes:
# FlightData,
# NotificationManager

from data_manager import DataManager
from flight_search import FlightSearch

# creating objects
data_manager = DataManager()
flight_search = FlightSearch()

# getting flights sheet data
sheet_data = data_manager.get_sheet_data()

# getting all iata codes on sheet data
iata_codes = [data["iataCode"] for data in sheet_data]

# checking if any iata code is empty
if "" in iata_codes:
    # getting missing iata codes
    for data in sheet_data:
        flight_search.get_iata_code(city_name=data["city"])