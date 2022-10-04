import requests
import os
headers_sheety = {"Authorization": os.environ.get("TOKEN")}
sheety = os.environ.get("SHEETY")

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_designation_data(self):
        response = requests.get(url=sheety,headers=headers_sheety)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_designation_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(url=f"{sheety}/{city['id']}",json=new_data, headers=headers_sheety)
            print(response.text)