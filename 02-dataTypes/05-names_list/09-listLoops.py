# Loops & Lists

# The for loop is used to iterate over the elements of a list.
# Here's an example:

minecraft_npc: list[str] = ["Zombie", "Skeleton", "Creeper"]
for npc in minecraft_npc:
    print(f"{npc} is a Minecraft NPC.")

# the for loop will iterate over all of the elements in the list.
# The variable npc will be assigned to each element in turn, and then
# the code inside the loop body will execute.

# Here's another example with a for loop and if statement to identify specific
# npcs:

minecraft_npc: list[str] = ["Zombie", "Skeleton", "Creeper"]
for npc in minecraft_npc:
    if npc == "Zombie":
        print(f"{npc} has not seen you.")
    elif npc == "Skeleton":
        print(f"{npc} has not seen you")
    else:
        print(f"{npc} is going to explode, run!.")
