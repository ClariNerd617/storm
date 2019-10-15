from requests import get, HTTPError
from json import dumps, decoder
from geodata import get_location_from_address, get_coords
import string


def get_nws_api_url(test: bool = False):
    coords = get_coords(get_location_from_address())
    url = f"https://api.weather.gov/points/{coords[0]},{coords[1]}"
    try:
        r = get(url=url, verify=False)
        r.raise_for_status()
        return r if test else r.json().get("properties").get("forecastGridData")
    except HTTPError as http_err:
        print(http_err)
    except decoder.JSONDecodeError as json_err:
        print(json_err)
    except Exception as err:
        print(err)


def get_point_forecast_data(test: bool = False, url: string = get_nws_api_url()):
    try:
        r = get(url=url, verify=False)
        r.raise_for_status()
        return r if test else r.json()
    except HTTPError as http_err:
        print(http_err)
    except decoder.JSONDecodeError as json_err:
        print(json_err)
    except Exception as err:
        print(err)

# response = requests.get("https://api.weather.gov/gridpoints/GYX/41,12").json()
# response = requests.get(https://api.weather.gov/stations/42040/observations/latest).json()


def get_value(var: string):
    return round(get_point_forecast_data()["properties"][var]["values"][0]["value"], 2)


keys = [
    "temperature", "dewpoint", "maxTemperature", "minTemperature",
    "relativeHumidity", "apparentTemperature", "heatIndex", "windChill",
    "windDirection", "windSpeed", "windGust", "probabilityOfPrecipitation"
]

initial_values = [get_value(var=key) for key in keys]
initial_conditions = dict(zip(keys, initial_values))

print(dumps(initial_conditions, indent=2, sort_keys=True))
