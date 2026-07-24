# Dumps to JSON

# Dumps is used to convert a Python object into a JSON string.
import json
import os
from dataclasses import dataclass

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'mc_data.json')


@dataclass
class MinecraftData:
    id: int
    name: str
    health: int


def get_mc() -> MinecraftData:
    with open(file_path, "r") as f:
        mc_mob: dict = json.load(f)

        mob = mc_mob["Mob_1"]

        minecraft_data: MinecraftData = MinecraftData(
            id=mob["id"],
            name=mob["name"],
            health=mob["health"],
        )
        return minecraft_data


minecraft_data: MinecraftData = get_mc()
print(f"{minecraft_data.id}, {minecraft_data.name}, {minecraft_data.health}")
