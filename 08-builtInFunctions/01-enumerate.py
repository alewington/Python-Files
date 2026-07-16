# Enumerate Function

# The enumerate() function in Python is a built-in function that adds a
# counter to an iterable and returns it as an enumerate object.
# This is useful when you need both the index and the value of
# items in a loop.

# Example usage of enumerate()
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(index, value)

# Output:
# 0 a
# 1 b
# 2 c
