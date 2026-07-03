# Update Set

# Sets are mutable, which means we can add or remove elements from them.
# Let's see how to do that.
# We can use the add() method to add an element to a set.
# Here is an example:
mySet: set[int] = {1, 2, 3}
print(f"Original Set: {mySet}")
mySet.update({4, 5})  # Add multiple elements to the set
print(f"Updated Set: {mySet}")
# Original Set: {1, 2, 3}
# Updated Set: {1, 2, 3, 4, 5}
