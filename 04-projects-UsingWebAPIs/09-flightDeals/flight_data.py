import datetime as dt


class FlightData:
    def __init__(self,
                 departure_city,
                 departure_airport_code,
                 arrival_city,
                 arrival_airport_code,
                 departure_date,
                 arrival_date,
                 price,
                 stop_overs=0,
                 via_city=""):
        self.departure_city = departure_city
        self.departure_airport_code = departure_airport_code
        self.arrival_city = arrival_city
        self.arrival_airport_code = arrival_airport_code
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.stop_overs = stop_overs
        self.via_city = via_city
        self.price = price