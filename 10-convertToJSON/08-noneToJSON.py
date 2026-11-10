# None to JSON

# Dumps is used to convert a Python object into a JSON string.
import json

data: None = None

# Convert None to JSON and print
print(json.dumps(data))

# Output:
# null

# Notice that None is converted to null in JSON and is lower case,
# which is the equivalent of None in Python.
