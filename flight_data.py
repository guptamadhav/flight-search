import requests
import os
from datetime import datetime
today = datetime.now().date()
next_month = (today.month + 6)%12
if next_month<today.month:
    next_year = today.year + 1
else:
    next_year = today.year

TEQUILA_API_KEY = os.environ.get("TEQUILA_API")
TEQUILA_API_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
class FlightData:

    def find_flights(self,city):
        data = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": f"{today.day}/{today.month}/{today.year}",
            "date_to": f"{today.day}/{next_month}/{next_year}"
        }
        headers = {"apikey": TEQUILA_API_KEY}
        response = requests.get(url=TEQUILA_API_SEARCH_ENDPOINT, params=data, headers=headers)
        return response.json()["data"]
