import datetime
def timestamp():
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    return now