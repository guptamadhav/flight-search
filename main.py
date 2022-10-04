from data_manager import DataManager
from flight_data import FlightData
# from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_designation_data()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flightsearch = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flightsearch.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_designation_codes()

for city in sheet_data:
    lowest_price = city["lowestPrice"]
    flightdata = FlightData()
    flight_data = flightdata.find_flights(city["iataCode"])
    for row in flight_data:
        if row["price"]<lowest_price:
            date = row['local_departure'].split("T")
            data = f"{city['city']} - {row['price']} - {date[0]}"
            # sms = NotificationManager()
            # sms.send_message(data)
            print(data)
            break
