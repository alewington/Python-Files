# Boolean to JSON

# Dumps is used to convert a Python object into a JSON string.
import json

data: bool = True

# Convert boolean to JSON and print
print(json.dumps(data))

# Output:
# true

# Notice the lower case 'true' in the output, which is the JSON representation
# of a boolean value.
