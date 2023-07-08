from datetime import datetime

def get_datetime():
    return datetime.today().strftime("%Y-%m-%dT%H:%M:%S.000Z")