import datetime as dt

class FlightData:
    def __init__(self):
        today = dt.datetime.now()
        initial = today + dt.timedelta(days=15)
        final = today + dt.timedelta(days=180)
        self.date_initial = initial.strftime("%d/%m/%Y")
        self.date_final = final.strftime("%d/%m/%Y")
        self.departure_city = "Recife"
        self.departure_airport_code = "REC"
        self.max_stopovers = 0
        self.nights_in_dst_from = 3
        self.nights_in_dst_to = 6
        self.locale = "pt"
        self.price_to = 0
        self.curr = "BRL"
