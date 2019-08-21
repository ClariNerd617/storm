import os
from datetime import datetime

import googlemaps
import requests

google_maps_api_key = os.environ.get('google_maps_api_key')
SPACE = '+'


def get_current_location():
    return requests.post(
        f'https://www.googleapis.com/geolocation/v1/geolocate?key={google_maps_api_key}'
    ).json()


def get_coords(response):
    return [
        round(response['location']['lat'], 3),
        round(response['location']['lng'], 3)
    ]


def format_address():
    # street_number = 1600
    street_number = int(
        input(
            'Enter street number: '
        )
    )
    # street = f'Amphitheatre{SPACE}Parkway'
    street = input(
        'Enter Street (e.g. Spartan Way): '
    ).replace(' ', SPACE)
    # municipality = f'Mountain{SPACE}View'
    municipality = input(
        'Enter City/Town Name (e.g. Port Clyde): '
    ).replace(' ', SPACE)
    # state_abbrev = 'CA'
    state_abbrev = input(
        'Enter State Abbreviation (e.g. NH): '
    )
    return f'{street_number}\
                {SPACE}{street},\
                {SPACE}{municipality},\
                {SPACE}{state_abbrev}'


def get_location_from_address(address=format_address()):
    response = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json" + \
        f"?address={address}&key={google_maps_api_key}"
    )
    return response.json()['results'][0]['geometry']
