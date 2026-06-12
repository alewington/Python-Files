# Converting to a Set

# Converting to a set is useful when you want to eliminate duplicates
# from a list or any other iterable. Sets are unordered collections of
# unique elements.


# Checking sets can also be useful when we want to remove duplicates from
# a list
sample_list = [1, 2, 3, 4, 5, 1, 2, 3]  # list
unique_set = set(sample_list)  # converted to set
print(f"Original List: {sample_list}")
print(f"Unique Set: {unique_set}")