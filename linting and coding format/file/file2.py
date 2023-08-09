"""Create a function add_to_json that takes a filename
and a dictionary as input. The
function should read the JSON data from the file,
add the new dictionary to it, and
write the updated data back to the same file"""

import json


def add_to_json(file_name, newdata):
    """Function to add JSON

    Args:
        file_name (str): filename.
        newdata (str): New data.
    """
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            data = json.load(file)
        data.append(newdata)
        with open(file_name, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("Data has been added tot he JSON file successfully")
    except FileNotFoundError:
        print("Error:File not found")


FILENAME = "data.json"
NEWDATA = {"Name": "Rabin", "Age": 30}
add_to_json(FILENAME, NEWDATA)
