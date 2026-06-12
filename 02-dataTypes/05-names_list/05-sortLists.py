# Sorting Lists

# Sorting lists are done by 2 methods:
# 1. sort() - sorts the list in place
# 2. sorted() - returns a new list that is sorted,
# leaving the original list unchanged

names = ["End Dragon", "Steve", "Zombie", "Endermen", "Creeper", "Alex"]

# Using sort()
print("Original list:", names)

# Using sorted()
sorted_names = sorted(names)
print("Original list after sorted() call:", names)
# so no effect to orginal list is not sorted by sorted

print("Newly sorted list from sorted():", sorted_names)
# so new list is sorted by sorted

names.sort()
print("Sorted using sort():", names)
# Shows original list is sorted by sort

names.sort(reverse=True)
print("Original list after sorted() call but reversed:", names)
# Shows list is sorted by sort but now reversed (decending)
