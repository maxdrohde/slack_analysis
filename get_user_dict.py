from pathlib import Path
from tools import parse_json

def get_user_dict():
    # Get a dict of User IDs to real names
    user_file =  Path('./slack/users.json')
    user_json = parse_json(user_file)
    user_dict = {user['id']: user['profile']['real_name'] for user in user_json}
    user_dict['USLACKBOT'] = 'Slackbot'
    return user_dict
