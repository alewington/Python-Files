# Access a Dictionary


# A minecraft example would be
# { "key": "value", "key2": "value2" }
minecraft_biomes = {
                    "Pale_Garden": "#FFFFFF",
                    "Beach": "#00FFFF",
                    "Desert": "#EFE4B5",
                    "Forest": "#173A17",
                    "Taiga": "#2D682D",
                    "Swamp": "#96C696"}

# You can access a dictionary by
# 1. using the key name
print(minecraft_biomes["Pale_Garden"])  # returns #FFFFFF
print(minecraft_biomes)

# 2. using the index number (starting at zero)
values01 = list(minecraft_biomes.values())
print(values01)
print(values01[2])
