import os
from datetime import datetime
import string

import googlemaps
from requests import post, get, HTTPError
from urllib3 import exceptions, disable_warnings
from json import decoder

disable_warnings(exceptions.InsecureRequestWarning)

google_maps_api_key = os.environ["google_maps_api_key"]
SPACE = "+"


def get_current_location(test: bool = False):
    try:
        r = post(
            url=f"https://www.googleapis.com/geolocation/v1/geolocate?key={google_maps_api_key}",
            verify=False
        )
        r.raise_for_status()
        return r if test else r.json()
    except HTTPError as http_err:
        print(http_err)
    except decoder.JSONDecodeError as json_err:
        print(json_err)
    except Exception as err:
        print(err)


def get_coords(response):
    return [
        round(response["location"]["lat"], 3),
        round(response["location"]["lng"], 3)
    ]


def format_address():
    # street_number = 1600
    # street = f"Amphitheatre{SPACE}Parkway"
    # municipality = f"Mountain{SPACE}View"
    # state_abbrev = "CA"
    street_number = int(input("Enter street number: "))
    street = input("Enter Street (e.g. Spartan Way): ").replace(" ", SPACE)
    municipality = input("Enter City/Town Name (e.g. Port Clyde): ").replace(" ", SPACE)
    state_abbrev = input("Enter State Abbreviation (e.g. NH): ")
    return f"{street_number}{SPACE}{street},{SPACE}{municipality},{SPACE}{state_abbrev}"


def get_location_from_address(address: str = format_address(), test: bool = False):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    url += f"?address={address}&key={google_maps_api_key}"
    try:
        r = get(url=url,verify=False)
        r.raise_for_status()
        return r if test else r.json()["results"][0]["geometry"]
    except HTTPError as http_err:
        print(http_err)
    except decoder.JSONDecodeError as json_err:
        print(json_err)
    except Exception as err:
        print(err)
