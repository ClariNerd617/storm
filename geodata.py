import os
from datetime import datetime

import googlemaps
import requests

google_maps_api_key = os.environ['google_maps_api_key']
SPACE = '+'

def get_current_location():
    response = requests.post(
        f'https://www.googleapis.com/geolocation/v1/geolocate?key={google_maps_api_key}').json()
    return response


def get_coords(response):
    [lat, lon] = [round(response['location']['lat'], 3),
                  round(response['location']['lng'], 3)]
    return [lat, lon]


def format_address():
    street_number = 1600
    street = f'Amphitheatre{SPACE}Parkway'
    municipality = f'Mountain{SPACE}View'
    state_abbrev = 'CA'
    address = f'{street_number}{SPACE}{street},{SPACE}{municipality},{SPACE}{state_abbrev}'
    return address


def get_location_from_address(address = format_address()):
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_maps_api_key}').json()['results'][0]['geometry']
    return response


# print('Coords from address for Google HQ')
# print(f'{get_coords(get_location_from_address())[0]}°N, {get_coords(get_location_from_address())[1]}°E')

# print('Coords for my cubicle at MMK OSW')
# print(f'{get_coords(get_current_location())[0]}°N, {get_coords(get_current_location())[1]}°E')
