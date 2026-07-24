# Dictionary to JSON

# Dumps is used to convert a Python object into a JSON string.
import json

data: dict[str, int] = {"one": 1, "two": 2, "three": 3}

# Convert dictionary to JSON and print
print(json.dumps(data))

# Output:
# {"one": 1, "two": 2, "three": 3}
