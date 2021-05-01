# This file will need to use the this classes:

# FlightSearch,
# FlightData,
# NotificationManager

from data_manager import DataManager

data_manager = DataManager()
sheet = data_manager.get_sheet_data()
print(sheet)
