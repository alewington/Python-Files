# Loads

# Loads is used to convert a JSON string into a Python object.
import json

data: str = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON string to Python object and print
print(json.loads(data))

# Output:
# {'name': 'John', 'age': 30, 'city': 'New York'}

# Notice that the JSON string is converted into a Python dictionary.
# Loads is used to convert a JSON string into a Python object.

# What this means is that the JSON string is converted into a Python
# dictionary.
# It is what the "s" in "loads" stands for, which is "string".
# The "load" in "loads" stands for "load", which means to load a
# JSON string into a Python object.

# It is that straight forward but easily confused with "load" which is used to
# load a JSON file into a Python object.
