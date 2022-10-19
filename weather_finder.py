
import requests
from typing import Union
from geopy.geocoders import Nominatim

class WeatherFinder:

    geolocator = Nominatim(user_agent='geoapiExercises')

    def __init__(self):
        pass

    def get_location(self, place: Union[str, list]):
        if isinstance(place, list):
            return place
        loc = WeatherFinder.geolocator.geocode(place)
        # print(loc)
        if loc is not None:
            return (loc.latitude, loc.longitude)
        return loc

    def get_api_data(self, address: Union[None, tuple]) -> str:
        if address is None:
            return None
        url = f'https://api.open-meteo.com/v1/forecast?latitude={address[0]}&longitude={address[1]}&current_weather=true'
        api_data = requests.get(url)
        return api_data.json()['current_weather']

    def get_weather(self, user_input: str):
        address = self.get_location(user_input)
        relevant_info = self.get_api_data(address)
        relevant_info['location'] = WeatherFinder.geolocator.reverse(address, addressdetails=True).raw
        return relevant_info
