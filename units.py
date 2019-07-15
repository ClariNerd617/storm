def c_to_f(temp_c):
    temp_f = round(((temp_c * (9/5)) + 32), 2)
    return temp_f


def f_to_c(temp_f):
    temp_c = round((temp_f - 32) * (5/9), 2)
    return temp_c


def m_to_in(amt_m):
    amt_in = round(amt_m * 39.3701, 2)
    return amt_in


def pa_to_mb(press_pa):
    #mb is hPa
    press_mb = round(press_pa / 100, 2)
    return press_mb


def mps_to_mph(speed_mps):
    speed_mph = round(speed_mps * 2.23694, 2)
    return speed_mph


def mph_to_kt(speed_mph):
    speed_kt = round(speed_mph * 0.868976, 2)
    return speed_kt


def mps_to_kph(speed_mps):
    speed_kph = round(speed_mps * 3.6, 2)
    return speed_kph


def mps_to_kt(speed_mps):
    speed_kt = mph_to_kt(mps_to_mph(speed_mps))
    return speed_kt


def m_to_mi(dist_m):
    dist_mi = round(dist_m * 0.000621371, 2)
    return dist_mi