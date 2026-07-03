# Set a Tuple

# A tuple is a sequence of values, often used in computer programming
# to group together multiple values that are related to each other.
# Tuples can be thought of as an immutable list, meaning that once
# they are created, their elements cannot be changed. In many
# programming languages, tuples are also known as "tuples" or
# "tuple pairs".

# Tuples are often used in situations where you need to group together
# multiple values that are related to each other, but you don't want
# to create a new data structure like a list.

# Tuples can also be used to create a fixed number of values that are
# related to each other, but you don't want to allow modification of
# those values.

# Creating a tuple
point: tuple[int, int] = (10, 20)

# Accessing elements in a tuple
x: int = point[0]
y: int = point[1]

# [0] denotes the position, for the example 0 represents the first position
print(point[0])
# [1] denotes the second position.
print(point[1])

# Empty tuple
empty_tuple: tuple[()] = ()
print(empty_tuple)

# Tuple with a single element
single_element_tuple: tuple[int] = (42,)  # Note the trailing comma
print(single_element_tuple)

# Unpacking a tuple
x, y = point
print(point)
print(x)
print(y)
