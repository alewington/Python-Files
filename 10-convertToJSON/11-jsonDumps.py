# Dumps To JSON

# Dumps is used to convert a Python object into a JSON string.
import json
data: dict[str, str] = {"name": "Creeper", "Health": "20", "speed": "1.0"}

# Convert dictionary to JSON and print
print(json.dumps(data))

# Output:
# {"name": "Creeper", "Health": "20", "speed": "1.0"}

# The "s" in "dumps" stands for "string", which means that the output is a
# JSON string.
# So this dumps function is used to convert a Python object into a JSON string.


# Not to be confused with "dump" which is used to convert a Python object into
# a JSON file.
