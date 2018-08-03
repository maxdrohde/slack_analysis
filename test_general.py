# pytest testing functions

from parse_json import load_messages

messages = load_messages()

def test_length():
    # Verify the correct number of messages
    length = len(messages)
    assert length == 2402
