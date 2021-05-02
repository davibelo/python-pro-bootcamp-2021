# This file will need to use the this classes:
# FlightData,
# NotificationManager

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

# creating objects
data_manager = DataManager()
flight_search = FlightSearch()

# getting sheet data
print("getting sheet data...")
sheet_data = data_manager.get_sheet_data()

# checking if any iata code is empty
if "" in [data["iataCode"] for data in sheet_data]:
    # getting missing iata codes
    for data in sheet_data:
        print("getting missing iata code...")
        data["iataCode"] = flight_search.get_iata_code(city_name=data["city"])
    # update sheet
    for data in sheet_data:
        print("update iata code on sheet...")
        data_manager.update_data(item_id=data["id"],
                                 item_key="iataCode",
                                 item_value=data["iataCode"])
else:
    print("iata codes ok")

for data in sheet_data:
    try:
        result = flight_search.get_flight_prices(
            destiny_airport_code=data["iataCode"],
            price_limit=data["lowestPrice"])
    except IndexError:
        print(f"no flights deals found for destination {data['city']}")
    else:
        print(result)
