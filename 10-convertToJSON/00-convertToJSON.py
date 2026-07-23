# convert to JSON

# This code snippet demonstrates how to convert a Python object to a JSON
# string.
# It uses the built-in json module.
import json


# Example Python object
data = {
    'name': 'Steve',
    'age': 30,
    'is_Mob': False,
    'has_unlocked': ['sword', 'shield', 'potion']
}

# Convert Python object to JSON string
json_string = json.dumps(data)
# dumps, the s stands for string, converts to a JSON string

# Print JSON string
print(json_string)
