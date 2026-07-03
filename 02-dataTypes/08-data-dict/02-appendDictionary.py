# Modify a Dictionary

# How to append a dictionary
minecraft_biomes: dict[str, str] = {
                    "Pale_Garden": "#FFFFFF",
                    "Beach": "#00FFFF",
                    "Desert": "#EFE4B5",
                    "Forest": "#173A17",
                    "Taiga": "#2D682D",
                    "Swamp": "#96C696"}

# This dictionary can be appended by
print(minecraft_biomes)

minecraft_biomes["Snowy Tundra"] = "#ccffcc"
print(minecraft_biomes)

# Adding the mountains colour would be
minecraft_biomes["Mountain"] = "#FF0000"
print(minecraft_biomes)
