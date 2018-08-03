# slack_to_csv

## Overview

Slack allows users to download the data from their workspace in the form of JSON files. This script navigates the directory structure of the Slack data files and parses the JSON into `Message` objects, which can be written to a CSV file. Currently the attributes supported are:

- channel
- user
- text
- subtype
- date_str

## Data Directory
You should have your data in a folder called `slack`.

Otherwise, in the file `parse_json.py`, you can change the name of your data directory by editing the global variable `DATA_FOLDER_NAME`

## Create CSV
To create a CSV file of the data, run:
```bash
python write_csv.py
```

## Load as Python list
To load the `Message` objects as a Python `list`, use:

```python
from parse_json import load_messages

messages = load_messages()

for m in messages:
    print(f'Text: {m.text} | Date: {m.date_str}')
```
