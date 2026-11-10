# List to JSON

# Dumps is used to convert a Python object into a JSON string.
import json

data: list[int] = [1, 2, 3, 4, 5]

# Convert list to JSON and print
print(json.dumps(data))

# Output:
# [1, 2, 3, 4, 5]
