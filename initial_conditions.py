import requests
from json import dumps
from geodata import get_location_from_address, get_coords


def get_nws_api_url():
    coords = get_coords(
        get_location_from_address()
    )
    url = f'https://api.weather.gov/points/{coords[0]},{coords[1]}'
    g = requests.get(
        url
    ).json()
    napi_url = g['properties']['forecastGridData']
    return napi_url


response = requests.get(
    get_nws_api_url()
).json()
# response = requests.get('https://api.weather.gov/gridpoints/GYX/41,12').json()
# response = requests.get(https://api.weather.gov/stations/42040/observations/latest).json()


def get_value(var):
    val = round(
        response['properties'][f'{var}']['values'][0]['value'],
        2
    )
    return val


keys = [
    'temperature', 'dewpoint', 'maxTemperature', 'minTemperature',
    'relativeHumidity', 'apparentTemperature', 'heatIndex', 'windChill',
    'windDirection', 'windSpeed', 'windGust', 'probabilityOfPrecipitation'
]

initial_values = []
for key in keys:
    initial_values.append(
        get_value(
            key
        )
    )

initial_conditions = dumps(
    dict(
        zip(
            keys,
            initial_values
        )
    ),
    indent=1
)

print(initial_conditions)
