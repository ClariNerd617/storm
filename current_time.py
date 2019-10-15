from datetime import datetime


def timestamp():
    return datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
