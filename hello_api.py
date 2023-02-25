from pprint import pprint
import requests

census_key = '314c1434f593fefe10432989ca9a141b83869fa1'




# """
# State printout and selection
# """

# list_of_states_url = f'https://api.census.gov/data/2020/dec/pl?get=NAME&for=state:*&key={census_key}'

# print('List of states:')
# list_of_states_data = requests.get(list_of_states_url).json()

# list_of_states = list_of_states_data[1:]

# for state in list_of_states:
#     print(state[0])

# print('To search for the population of a city.')
# user_state_selection = input('Enter the state: ')

# user_selected_state_code = ''
# for state in list_of_states:
#     if (user_state_selection == state[0]):
#         user_selected_state_code = state[1]

# print(user_selected_state_code)

# """
# County printout and selection
# """

# list_of_counties_url = f'https://api.census.gov/data/2020/dec/pl?get=NAME&for=county:*&in=state:{user_selected_state_code}&key={census_key}'

# print('List of counties for selected state:')
# list_of_counties_data = requests.get(list_of_counties_url).json()

# list_of_counties = list_of_counties_data[1:]

# for county in list_of_counties:
#     print(county[0])

# user_county_selection = input('Enter the county: ')

# user_selected_county_code = ''
# for county in list_of_counties:
#     if (user_county_selection == county[0]):
#         user_selected_county_code = county[2]



# """
# County subdivision and selection
# Subdivision needs %20 after county
# """

# list_of_subdivisions_url = f'https://api.census.gov/data/2020/dec/pl?get=NAME&for=county%20subdivision:*&in=state:{user_selected_state_code}&in=county:{user_selected_county_code}&key={census_key}'

# print('List of county subdivisions for selected county:')
# list_of_subdivisions_data = requests.get(list_of_subdivisions_url).json()

# list_of_county_subdivisions = list_of_subdivisions_data[1:]

# for subdivision in list_of_county_subdivisions:
#     print(subdivision[0])

# user_county_subdivision_selection = input('Enter the subdivision: ')

# user_selected_subdivision_code = ''
# for subdivision in list_of_county_subdivisions:
#     if (user_county_subdivision_selection == subdivision[0]):
#         user_selected_subdivision_code = subdivision[3]

# print(user_selected_subdivision_code)


"""
Population section
NAME is the selected area [0]
P1_001N is the total population [1]
H1_001N is the total housing number [2]
H1_002N is the total occupied homes [3]
H1_003N is the total vacant homes [4]
P1_004N is the total black population []
P2_002N is the total hispanic population []
P1_006N is the total asian populaiton []
P1_003N is the total white population []
"""

# user_selection_population_url = f'https://api.census.gov/data/2020/dec/pl?get=NAME,P1_001&for=county%20subdivision:{user_selected_subdivision_code}&in=state:{user_selected_state_code}&in=county:{user_selected_county_code}&key={census_key}'
user_selection_population_url = f'https://api.census.gov/data/2020/dec/pl?get=NAME,P1_001N,H1_001N,H1_002N,H1_003N,P1_004N,P2_002N,P1_006N,P1_003N&for=county%20subdivision:55852&in=state:27%20county:123&key={census_key}'

population_data = requests.get(user_selection_population_url).json()

city_data = population_data[1]
print(city_data)
city_name = city_data[0]
total_city_population = city_data[1]
total_housing = city_data[2]
total_occupied_homes = city_data[3]
total_vacant_homes = city_data[4]
black_population = city_data[5]
hispanic_population = city_data[6]
asian_population = city_data[7]
white_population = city_data[8]


print(f'{city_name} has a total population of {total_city_population}.')
print(f'Out of the {total_housing} houses: {total_occupied_homes} are occupied and {total_vacant_homes} are vacant.')
print(f'The racial breakdown of the city is:\n   {black_population} Black or African American\n   {hispanic_population} Hispanic or Latino\n   {asian_population} Asian\n   {white_population} White.')

"""
This api section is for the change is population in an area between 2020 and 2021
"""