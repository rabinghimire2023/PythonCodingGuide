"""Create a function add_to_json that takes a filename and a dictionary as input. The
function should read the JSON data from the file, add the new dictionary to it, and
write the updated data back to the same file"""

import json
def add_to_json(filename,new_data):
    try:
        with open(filename,'r') as file:
            data=json.load(file)
        data.append(new_data)
        with open(filename,'w') as file:
            json.dump(data,file,indent=4)
        print("Data has been added tot he JSON file successfully")
    except FileNotFoundError:
        print("Error:File not found")
    except Exception as e:
        print(f"Error:{e}")
        
filename="data.json"
new_data={"Name":"Rabin","Age":30}
add_to_json(filename,new_data)
    