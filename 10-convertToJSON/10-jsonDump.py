# Dumps to JSON

# Dumps is used to convert a Python object into a JSON string.
import json
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'mc_data2.json')

Mob_2: dict[str, int | str] = {
    "id": 2,
    "name": "Zombie",
    "health": 20,
}

with open(file_path, "w") as f:
    json.dump(Mob_2, f, indent=4)

# indent is used to format the JSON string with indentation for better
# readability.
# Without it the JSON string will be a single line, which can be hard to read.
