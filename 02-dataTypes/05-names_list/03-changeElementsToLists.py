# Add Elements to Lists

# To change the elements of a list, you can use an index and assignment
# operator (=).

# Example
minecraft_npc: list[str] = ["Creeper", "Skeleton"]
print(minecraft_npc)  # ['Creeper', 'Skeleton']

minecraft_npc[1] = "Zombie"
print(minecraft_npc)  # ['Creeper', 'Zombie']

# minecraft[1] = "Zombie" means:
# - Get the element at index 1 (the second element) of the list
#   minecraft.
# - Assign the string "Zombie" to that element.

# You can also use a slice to change multiple elements in a list.

# Example
minecraft_npc: list[str] = ["Creeper", "Skeleton"]
print(minecraft_npc)  # ['Creeper', 'Skeleton']

minecraft_npc[1:] = ["Zombie", "Spider"]
print(minecraft_npc)  # ['Creeper', 'Zombie', 'Spider']

# minecraft_npc[1:] means:
# - Get all the elements from index 1 (the second element) to the end of the
#   list.
# - Assign the new list ["Zombie", "Spider"] to those elements.
