# Intersection of two sets

# The intersection of two sets is a new set that contains only the elements
# that are present in both sets. In Python, you can use the `&` operator or
# the `intersection()` method to find the intersection of two sets.
set1: set[int] = {1, 2, 3, 4}
set2: set[int] = {3, 4, 5, 6}
print(f"{set1=}")
print(f"{set2=}")

# Using the & operator
intersection_set = set1 & set2
print(f"Intersection using & operator: {intersection_set}")

# Using the intersection() method
intersection_set_method = set1.intersection(set2)
print(f"Intersection using intersection() method: {intersection_set_method}")

# Both methods will give you the same result, which is a new set
# containing the elements that are present in both `set1` and `set2`.
# In this case, the intersection will be `{3, 4}`.
