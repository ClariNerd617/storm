# TODO Refactor with a map or a dict switcher or a lambda or something

def c_to_f(temp_c):
    return round(((temp_c * (9/5)) + 32), 2)


def f_to_c(temp_f):
    return round((temp_f - 32) * (5/9), 2)


def m_to_in(amt_m):
    return round(amt_m * 39.3701, 2)


def pa_to_mb(press_pa):
    # mb is hPa
    return round(press_pa / 100, 2)


def mps_to_mph(speed_mps):
    return round(speed_mps * 2.23694, 2)


def mph_to_kt(speed_mph):
    return round(speed_mph * 0.868976, 2)


def mps_to_kph(speed_mps):
    return round(speed_mps * 3.6, 2)


def mps_to_kt(speed_mps):
    return mph_to_kt(mps_to_mph(speed_mps))


def m_to_mi(dist_m):
    return round(dist_m * 0.000621371, 2)
