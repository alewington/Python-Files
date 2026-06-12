# Lists

# Lists are ordered collections of items. Items can be of different types.
# For example, a list could contain strings, integers, and even other lists.
names = ["Steve", "Alex"]
print(names)

# 1. Accessing List Elements
print(names[0])

# 2. Modifying List Elements
names.append("Ender Dragon")
print(names)

# 3. Pop the last name from the list
names.pop()
print(names)

# 4. Sort list descending alphabetically
names.sort(reverse=True)
print(names)
