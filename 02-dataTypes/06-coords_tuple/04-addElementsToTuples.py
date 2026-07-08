# Addd elements to a tuple

# Add elements to a tuple
# 1. Create an empty tuple
# 2. Add elements to the tuple
# 3. Print the tuple

# Create an empty tuple
emptyTuple: tuple[int, ...] = ()
print(type(emptyTuple))  # <class 'tuple'>

# Create a non-empty tuple
nonEmptyTuple: tuple[str, ...] = ("Hello", "World")
print(type(nonEmptyTuple))  # <class 'tuple'>

# Add an element to the empty tuple
emptyTuple += (1,)
print(emptyTuple)  # (1,)

# Add elements to the non-empty tuple
nonEmptyTuple += ("!", "?")
print(nonEmptyTuple)   # ('Hello', 'World', '!', '?')

# another method to add elements to a tuple is
# by using the append() function. This function
# adds an element at the end of the list

anotherEmptyTuple: tuple[int, ...] = ()
print(type(anotherEmptyTuple))  # <class 'tuple'>
anotherNonEmptyTuple: tuple[str, ...] = ("Hello", "World")
print(type(anotherNonEmptyTuple))  # <class 'tuple'>
