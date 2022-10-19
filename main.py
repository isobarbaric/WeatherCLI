
from weather_finder import WeatherFinder
from colorama import Fore

import typer
import geocoder

app = typer.Typer()
data = WeatherFinder()

# {'temperature': 3.3, 'windspeed': 17.8, 'winddirection': 223.0

def present_data(weather_data: dict):
# {'place_id': 34600901, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright', 'osm_type': 'way', 'osm_id': 177927457, 'lat': '43.54594235', 'lon': '-80.25599364166666', 'display_name': '65, Liverpool Street, Guelph Junction, Guelph, Southwestern Ontario, Ontario, N1H 4J7, Canada', 'address': {'house_number': '65', 'road': 'Liverpool Street', 'neighbourhood': 'Guelph Junction', 'city': 'Guelph', 'state_district': 'Southwestern Ontario', 'state': 'Ontario', 'ISO3166-2-lvl4': 'CA-ON', 'postcode': 'N1H 4J7', 'country': 'Canada', 'country_code': 'ca'}, 'boundingbox': ['43.54589235', '43.54599235', '-80.256043641667', '-80.255943641667']}

    weather_psa = Fore.BLUE + "Weather!\n"

    parsed_location = f"{weather_data['location']['address']['house_number']} {weather_data['location']['address']['road']}, {weather_data['location']['address']['city']}, {weather_data['location']['address']['country']}"

    weather_psa += f'  - 🌡  The temperature at {parsed_location} is {weather_data["temperature"]}° C!\n'

    # add more fields

    print(weather_psa)

@app.command()
def weather(address: bool = False):
    if (address):
        custom_address = input('Please enter the address: ')
        weather_data = data.get_weather(custom_address)
        present_data(weather_data=weather_data)
    else:
        g = geocoder.ip('me')
        weather_data = data.get_weather(g.latlng)
        present_data(weather_data=weather_data)

if __name__ == '__main__':
    app()
