# Unions

# Unions are used to combine multiple sets into one, removing any
# duplicate elements. This can be useful when you need to
# combine data from different sources and ensure that each
# element appears only once.

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)
print(union_set)

# Checking sets can also be useful when we want to find the intersection of
# two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)
print(f"Intersection: {intersection}")
