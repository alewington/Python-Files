# Convert a string to JSON

import json
# Sample string
string_data: str = '{"Name": "Steve"}'

print(json.loads(string_data))
# Convert string to JSON and print

# Output:
# {'Name': 'Steve'}
