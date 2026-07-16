# Sorting Lists

# Sorting lists are done by 2 methods:
# 1. sort() - sorts the list in place
# 2. sorted() - returns a new list that is sorted. This leaves
# the original list unchanged.

names: list[str] = [
    "End Dragon",
    "Steve",
    "Zombie",
    "Endermen",
    "Creeper",
    "Alex",
]

# Using sort()
print("Original list:", names)

# Using sorted()
sorted_names = sorted(names)
print("Original list after sorted() call:", names)
# so no effect: the original list is not sorted by sorted()

print("Newly sorted list from sorted():", sorted_names)
# so new list is sorted by sorted
