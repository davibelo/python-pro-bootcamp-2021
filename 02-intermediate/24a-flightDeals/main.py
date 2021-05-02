from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import datetime as dt

DAYS_MIN = 15
DAYS_INTERVAL = 180

DEP_CITY = "Recife"
DEP_AIRPORT_CODE = "REC"
MAX_STOP_OVER = 0
NIGHTS_MIN = 3
NIGHTS_MAX = 6
LANGUAGE = "pt"
CURRENCY = "BRL"

# calculating dates for flight search
today = dt.datetime.now()
initial = today + dt.timedelta(days=DAYS_MIN)
final = today + dt.timedelta(days=DAYS_INTERVAL)
date_initial = initial.strftime("%d/%m/%Y")
date_final = final.strftime("%d/%m/%Y")

# creating objects
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

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
            departure_code=DEP_AIRPORT_CODE,
            arrival_code=data["iataCode"],
            max_stops=MAX_STOP_OVER,
            date_initial=date_initial,
            date_final=date_final,
            nights_min=NIGHTS_MIN,
            nights_max=NIGHTS_MAX,
            language=LANGUAGE,
            price_limit=data["lowestPrice"],
            currency=CURRENCY)
    except IndexError:
        try:
            result = flight_search.get_flight_prices(
                departure_code=DEP_AIRPORT_CODE,
                arrival_code=data["iataCode"],
                max_stops=MAX_STOP_OVER+1,
                date_initial=date_initial,
                date_final=date_final,
                nights_min=NIGHTS_MIN,
                nights_max=NIGHTS_MAX,
                language=LANGUAGE,
                price_limit=data["lowestPrice"],
                currency=CURRENCY)
        except IndexError:
            print(f"no flights deals found for destination {data['city']}")
        else:
            alert = f"Alert! Flight from {result.departure_city} ({result.departure_airport_code}) to {result.arrival_city} ({result.arrival_airport_code}) from {result.departure_date} to {result.arrival_date}, stop overs: {result.stop_overs}, via: {result.via_city}, price: {CURRENCY} {result.price}"
            notification_manager.send_SMS(text=alert)
    else:
        alert = f"Alert! Flight from {result.departure_city} ({result.departure_airport_code}) to {result.arrival_city} ({result.arrival_airport_code}) from {result.departure_date} to {result.arrival_date}, stop overs: {result.stop_overs}, price: {CURRENCY} {result.price}"
        notification_manager.send_SMS(text=alert)