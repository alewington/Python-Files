# List Methods

# List Methods are functions that can be applied to a list.
# Some of the most common ones are:
# - append() - adds an item to the end of a list.
# - pop() - removes and returns an item from the end of a list.
# - remove() - removes the first instance of a specified value from a list.
# - insert() - inserts an item at a specific position in a list.
# - sort() - sorts the items in a list in ascending order.
# - reverse() - reverses the order of items in a list.
# - count() - returns the number of times a specified value occurs in a list.
# - index() - returns the position of the first occurrence of a specified
#             value in a list.
# - extend() - adds the contents of one list to the end of another.

# Let's see some examples:

minecraft_npc: list[str] = ["Zombie", "Skeleton", "Creeper"]
print(f"The minecraft npc are {minecraft_npc}")

# append() - adds an item to the end of a list.
minecraft_npc.append("Wither Skeleton")
print(f"The minecraft npc are {minecraft_npc}")

# pop() - removes and returns an item from the end of a list.
last_item = minecraft_npc.pop()
print(f"The last item is: {last_item}")
print(f"The minecraft npc are {minecraft_npc}")

# remove() - removes the first instance of a specified value from a list.
minecraft_npc.remove("Zombie")
print(f"The minecraft npc are {minecraft_npc}")

# insert() - inserts an item at a specific position in a list.
minecraft_npc.insert(0, "Zombie")
print(f"The minecraft npc are {minecraft_npc}")

# sort() - sorts the items in a list in ascending order.
minecraft_npc.sort()
print(f"The minecraft npc are {minecraft_npc}")

# reverse() - reverses the order of items in a list.
minecraft_npc.reverse()
print(f"The minecraft npc are {minecraft_npc}")

# count() - returns the number of times a specified value occurs in a list.
print("How many Skeletons?")
print(minecraft_npc.count("Skeleton"))

# index() - returns the position of the first occurrence of a specified
#           value in a list.
print("Where is the Wither Skeleton?")
print(minecraft_npc.index("Wither Skeleton"))

# extend() - adds the contents of one list to the end of another.
other_npc: list[str] = ["Slime", "Enderman"]
minecraft_npc.extend(other_npc)
print(f"The minecraft npc are {minecraft_npc}")
