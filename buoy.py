import requests
import json
import pygments

print(
    json.dumps(
        requests.get(
            'https://api.weather.gov/stations/42040/observations/latest').json(), indent=1))