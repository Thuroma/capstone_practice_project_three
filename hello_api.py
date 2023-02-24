from pprint import pprint
import requests

census_key = '314c1434f593fefe10432989ca9a141b83869fa1'




"""
State printout and selection
"""

list_of_states_url = f'https://api.census.gov/data/2020/dec/pl?get=NAME&for=state:*&key={census_key}'

print('List of states:')
list_of_states_data = requests.get(list_of_states_url).json()

list_of_states = list_of_states_data[1:]

for state in list_of_states:
    print(state[0])

print('To search for the population of a city.')
user_state_selection = input('Enter the state: ')

user_selected_state_code = ''
for state in list_of_states:
    if (user_state_selection == state[0]):
        user_selected_state_code = state[1]

print(user_selected_state_code)

"""
County printout and selection
"""

list_of_counties_url = f'https://api.census.gov/data/2020/dec/pl?get=NAME&for=county:*&in=state:{user_selected_state_code}&key={census_key}'

print('List of counties for selected state:')
list_of_counties_data = requests.get(list_of_counties_url).json()

list_of_counties = list_of_counties_data[1:]

for county in list_of_counties:
    print(county[0])

user_county_selection = input('Enter the county: ')

user_selected_county_code = ''
for county in list_of_counties:
    if (user_county_selection == county[0]):
        user_selected_county_code = county[1]


"""
County subdivision and selection
"""

list_of_subdivisions_url = f'https://api.census.gov/data/2020/dec/pl?get=NAME&for=county%20subdivision:*&in=state:27&in=county:{user_selected_county_code}&key={census_key}'




















# print('List of county subdivisions for selected county:')
# list_of_subdivisions_data = requests.get(list_of_subdivisions_url).json()
# pprint(list_of_subdivisions_data)



# total_pop_county_url = f'https://api.census.gov/data/2020/dec/pl?get=NAME&for=county:123&in=state:27&key={census_key}'
# total_pop_county_subdivision_url = f'https://api.census.gov/data/2020/dec/pl?get=NAME,P1_001N&for=county%20subdivision:55852&in=state:27&in=county:123&key={census_key}'

# # Prints the population for a given county
# print('Total population for Ramsay county:')
# total_pop_county_data = requests.get(total_pop_county_url).json()
# pprint(total_pop_county_data)

# # Prints the population for a given subdivision
# print('Total population for Ramsay county subdivisions:')
# total_pop_county_subdivision_data = requests.get(total_pop_county_subdivision_url).json()
# pprint(total_pop_county_subdivision_data)