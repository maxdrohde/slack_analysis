from parse_json import load_messages
import pandas as pd

messages = load_messages()

message_dicts = [vars(message) for message in messages]

df = pd.DataFrame(message_dicts)
df = df[['channel', 'user','text', 'subtype', 'date_str']]

df.to_csv('slack_data.csv')
