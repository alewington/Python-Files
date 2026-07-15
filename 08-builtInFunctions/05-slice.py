# Slice function

# The slice() function returns a slice object representing a set of indices
# specified by range(start, stop, step).
# Example usage of slice()
my_list = [0, 1, 2, 3, 4, 5]
my_slice = slice(2, 5)
print(my_list[my_slice])  # Output: [2, 3, 4]

# You can also specify a step value
my_slice_with_step = slice(1, 6, 2)
print(my_list[my_slice_with_step])  # Output: [1, 3, 5]
