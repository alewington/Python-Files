# Joining lists

minecraft_npc = ["Zombie", "Skeleton", "Creeper"]
mincraft_npc_2 = ["Blaze", "Witch", "Spider"]

print("List 1:")
print(minecraft_npc)
print("List 2:")
print(mincraft_npc_2)

# Join the lists together to make a new list
combined = minecraft_npc + mincraft_npc_2
print("\nCombined List:")
print(combined)

# or

combined = minecraft_npc.extend(mincraft_npc_2)
print("\nCombined List:")
print(combined)
