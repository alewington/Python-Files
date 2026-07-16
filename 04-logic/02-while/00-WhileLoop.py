# While Loop

# When to use a while loop?
# -----------------------
# - A while loop is used when you don't know how many times the loop will run.
# - It runs until a condition is met.
# - To keep asking for input until they provide a valid value (condition is
# met)
# - Infinite loops with exit ( this is dangerous but useful when done
# correctly)
# - state driven or event-driven loops


# Don't

# Always ensure the condition will eventually become False to avoid infinite
# loops
# Break or time out the loop if it takes too long.
# Use for loops when you know the exact number of iterations ( may have to be
# calculated) Safer and more readable


# Quick Guide

# Use for when you know the number of loops
# Use while when you know when to stop, not how many times.

# Example:

# no infinite while loop example that loops a few times based on a list with
# names in
names = ["Steve", "Axolotl", "Chicken"]
while len(names) > 0:
    print("Hello " + names[0])
    del names[0]
else:
    print("No more names to say hello to")
# Hello Steve
# Hello Axolotl
# Hello Chicken
# No more names to say hello to
