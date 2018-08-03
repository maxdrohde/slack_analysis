from pathlib import Path
from message import Message
from tools import *
from get_user_dict import get_user_dict

DATA_FOLDER_NAME = 'slack'
p = Path('./' + DATA_FOLDER_NAME) # path to data folder

def load_message_object(message_dict, channel):
    # Given a list of attributes -> loads the message object from the message dict
    attributes = ['text', 'files', 'subtype', 'user', 'ts']
    user_dict = get_user_dict()

    message = Message()
    for attribute in attributes:
        if attribute in message_dict:
            value = message_dict[attribute]
            if attribute == 'user':
                value = user_dict[value]
            setattr(message, attribute, value)
    message.channel = channel
    message.dt = ts_to_datetime(message.ts)
    message.date_str = ts_to_date_str(message.ts)
    return message

def load_messages():
    # Get paths for all channel directories --> [<dir_path_1>, <dir_path_2>, ...]
    channel_dirs = [channel_dir for channel_dir in p.iterdir() if channel_dir.is_dir()]

    # Create dict {channel_name : [list of json file paths]}
    channel_files = {channel_dir.name : list(channel_dir.glob('*.json')) for channel_dir in channel_dirs}

    messages = []
    for channel, files in channel_files.items():
        for file in files:
            jsons = parse_json(file)
            for message_dict in jsons:
                message = load_message_object(message_dict, channel)
                messages.append(message)
    return messages
