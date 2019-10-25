from datetime import datetime, timezone


def timestamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d_%H:%M:%S')
