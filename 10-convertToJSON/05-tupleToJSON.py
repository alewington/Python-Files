# Tuple to JSON

# Dumps is used to convert a Python object into a JSON string.
import json

data: tuple[int, str, float] = (1, "Hello", 3.14)

# Convert tuple to JSON and print
print(json.dumps(data))

# Output:
# [1, "Hello", 3.14]
