import requests
from pprint import pprint

census_key = '314c1434f593fefe10432989ca9a141b83869fa1'


list_of_consolidated_cities_url = f'https://api.census.gov/data/2020/dec/pl?get=NAME&for=consolidated%20city:*&in=state:27&key={census_key}'

city_data = requests.get(list_of_consolidated_cities_url).json()
pprint(city_data)