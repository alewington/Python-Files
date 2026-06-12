# Removing Elements from a list

# There are different ways tyo remove elements from a list these are 4 of them:
# - Remove by index
# - Remove by value
# - Remove using pop()
# - Clear all elements from list

# 1. Remove an element by its index
names = ['Creeper', 'Bob', 'Charlie', 'Steve', 'Alex']
removed_name = names.pop(1)  # Removes 'Bob' and returns it
print(f"Removed Name: {removed_name}")
print(f"Remaining Names: {names}")

# 2. Remove an element by value
names.remove('Charlie')  # Removes the first occurrence of 'Charlie'
print(f"Updated Names List: {names}")

# 3. Remove elements using a loop
while 'Creeper' in names:
    names.remove('Creeper')
print(f"Final Names List: {names}")

# 4. Clear a list (Remove all elements)
names.clear()  # Removes all elements from the list
print(f"Cleared List: {names}")
