# zip Function

# The zip() function in Python is a built-in function that takes multiple
# iterables (like lists or tuples) and aggregates them into a single iterable
# of tuples. Each tuple contains elements from the input iterables that are
# at the same index.

# They must match in length, otherwise the resulting iterable will be as long
# as the shortest input iterable.

# Example usage of zip()
list_one = [1, 2, 3, 4, 5]
list_two = ['a', 'b', 'c', 'd', 'e']

zipped = zip(
    list_one,
    list_two
    )

print(list(zipped))  
# Output: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
