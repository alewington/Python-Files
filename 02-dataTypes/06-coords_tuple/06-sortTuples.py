# Sorting Tuples

# You can sort tuples by 1st element, 2nd element, etc. using() function
# or list.sort method.

example_coordinates: list[tuple[int, int]] = [(4, 5), (1, 0), (2, 7)]
example_coordinates = sorted(example_coordinates)
print(example_coordinates)  # Output: [(1, 0), (2, 7), (4, 5)]
