import json
from datetime import datetime

def ts_to_datetime(ts):
    # Convert from timestamp to datetime object
    ts = float(ts)
    dt = datetime.fromtimestamp(ts)
    return dt

def ts_to_date_str(ts):
    # Convert from timestamp to formatted date string
    ts = float(ts)
    date_str = datetime.fromtimestamp(ts).strftime("%A, %d %B %Y %I:%M%p")
    return date_str

def parse_json(json_path):
    # Parse a JSON file given the path
    with open(json_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data
