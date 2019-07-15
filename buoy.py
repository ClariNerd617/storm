from requests import get
import json
import units
import os
import current_time as ct

buoy_id = input('Enter Buoy ID Number e.g. 42040: ')
conditions = get(f'https://api.weather.gov/stations/{buoy_id}/observations/latest').json()['properties']

vars = [
    'timestamp',
    'temperature',
    'dew_point',
    'wind_direction',
    'wind_speed',
    'wind_gust',
    # 'baro_pressure',
    'slp',
    # 'visibility',
    # 'precip_past_hr',
    # 'precip_past_6hr',
    'rel_h'
    # 'wind_chill',
    # 'heat_index'
]


def save_data(data):
    if not os.path.isdir(f'saved_data/{buoy_id}'):
        os.system(f'mkdir saved_data/{buoy_id}')
    with open(f'saved_data/{buoy_id}/{ct.timestamp()}.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)


values = [
    ct.timestamp(),
    units.c_to_f(conditions['temperature']['value']),
    units.c_to_f(conditions['dewpoint']['value']),
    round(conditions['windDirection']['value']),
    units.mps_to_mph(conditions['windSpeed']['value']),
    units.mps_to_mph(conditions['windGust']['value']),
    # units.pa_to_mb(conditions['barometricPressure']['value']),
    units.pa_to_mb(conditions['seaLevelPressure']['value']),
    # units.m_to_mi(conditions['visibility']['value']),
    # units.m_to_in(conditions['precipitationLastHour']['value']),
    # units.m_to_in(conditions['precipitationLast6Hours']['value']),
    round(conditions['relativeHumidity']['value'], 2)
    # units.c_to_f(conditions['windChill']['value']),
    # units.c_to_f(conditions['heatIndex']['value'])
]

current_conditions = dict(zip(vars, values))

save_data(current_conditions)