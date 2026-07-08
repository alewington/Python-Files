# how to access elements in a tuple

# You can access elements in a tuple by using 0-based indexing, just like
# you do with lists and strings:

coordinates: tuple[int, ...] = (12, 5)  # we've created a tuple
# called coordinates
print(coordinates[0])  # prints 12
print(coordinates[1])  # 5

# You can also use negative indexing to access elements from the end of the
# tuple:

print(coordinates[-1])  # prints 5
print(coordinates[-2])  # prints 12

# You can't change a value in a tuple, but you can create a new one by adding
# or changing values.

new_coordinate: tuple[int, ...] = (30, 40)
print(new_coordinate)

# the following line will throw an error:

# coordinates[0] = 5  # this will throw an error
# print(coordinates)
