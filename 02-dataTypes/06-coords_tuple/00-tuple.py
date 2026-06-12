# Tuple

# Tuples are immutable ordered collections of items. They can contain 0 or
# more elements, and each element can be of any type.
# Tuples are defined using parentheses () instead of
# square brackets [] like lists.

# What does immutable mean? It means that once a tuple is created,
# its contents cannot be changed.

# Can a immutable object be replaced? Yes, the reference to the object can be
# replaced with another object.

# Creating a tuple
point = (10, 20)

# Accessing elements in a tuple
x = point[0]
y = point[1]

# Modifying a tuple
# point[0] = 30  # This will raise an error because tuples are immutable

# Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14)

# Empty tuple
empty_tuple = ()

# Tuple with a single element
single_element_tuple = (42,)  # Note the trailing comma

# Unpacking a tuple
x, y = point

# Length of a tuple
length = len(point)

# Checking if an item exists in a tuple
exists = 10 in point

# Iterating over a tuple
for element in point:
    print(element)
