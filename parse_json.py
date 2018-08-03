from pathlib import Path
from message import Message
import json
from datetime import datetime

DATA_FOLDER_NAME = 'slack'
p = Path('./' + DATA_FOLDER_NAME) # path to data folder

def ts_to_datetime(ts):
    ts = float(ts)
    dt = datetime.fromtimestamp(ts)
    return dt

def ts_to_date_str(ts):
    ts = float(ts)
    date_str = datetime.fromtimestamp(ts).strftime("%A, %d %B %Y %I:%M%p")
    return date_str

def parse_json(json_path):
    # Parses a JSON file given the path
    with open(json_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data

def load_message(message_dict):
    # Given a list of attributes -> loads the message object from the message dict
    attributes = ['text', 'files', 'subtype', 'user', 'ts']

    message = Message()
    for attribute in attributes:
        if attribute in message_dict:
            value = message_dict[attribute]
            if attribute == 'user':
                value = user_dict[value]
            setattr(message, attribute, value)
    return message

# Get a dict of User IDs to real names
user_file =  Path('./slack/users.json')
user_json = b = parse_json(user_file)
user_dict = {user['id']: user['profile']['real_name'] for user in user_json}
user_dict['USLACKBOT'] = 'Slackbot'

# Load the data files into Message objects
#-------------------------------------------------------------------------------
def load_messages():

    # Get paths for all channel directories
    channel_dirs = [channel_dir for channel_dir in p.iterdir() if channel_dir.is_dir()]

    # Create dict {channel_name : [list of json file paths]}
    channel_files = {channel_dir.name : list(channel_dir.glob('*.json')) for channel_dir in channel_dirs}

    messages = []
    for channel, files in channel_files.items():
        for file in files:
            jsons = parse_json(file)
            for message_dict in jsons:
                message = load_message(message_dict)
                message.channel = channel
                message.dt = ts_to_datetime(message.ts)
                message.date_str = ts_to_date_str(message.ts)
                messages.append(message)
    return messages
