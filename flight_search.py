import os
import requests

TEQUILA_ENDPOINT = os.environ.get("TEQUILA_ENDPOINT")
TEQUILA_API_KEY = os.environ.get("TEQUILA_API")

class FlightSearch():

    def get_destination_code(self, city_name):
        data = {"term": city_name,"location_types": "city"}
        headers = {"apikey": TEQUILA_API_KEY}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=headers, params=data)
        results = response.json()
        code = results["locations"][0]["code"]
        return code

