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

# Using sort
names.sort()
print("Sorted using sort():", names)
# Shows original list is sorted by sort

names.sort(reverse=True)
print("Original list after sorted() call but reversed:", names)
# Shows list is sorted by sort but now reversed (descending)
