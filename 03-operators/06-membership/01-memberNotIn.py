# Membership NOT IN

# The membership operator 'not in' is used to check if a value does not
# exist within a sequence (like a list, tuple, or string).
# It returns True if the value is not found in the sequence,
# otherwise it returns False.

# Example with a list
my_list: list[int] = [1, 2, 3, 4, 5]
print(3 not in my_list)  # Output: False, because 3 is present in the list
print(6 not in my_list)  # Output: True, because 6 is not present in the list

# Example with a string
my_string: str = "Hello, World!"
print("Hello" not in my_string)
# Output: False, because "Hello" is present in the string
print("Python" not in my_string)
# Output: True, because "Python" is not present in the string

# Example with a tuple
my_tuple: tuple[int, int, int] = (10, 20, 30)
print(20 not in my_tuple)
# Output: False, because 20 is present in the tuple
print(40 not in my_tuple)
# Output: True, because 40 is not present in the tuple

# Example with a set
my_set: set[int] = {100, 200, 300}
print(200 not in my_set)  # Output: False, because 200 is present in the set
print(400 not in my_set)  # Output: True, because 400 is not present in the set

# Example with a dictionary
my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}
print("a" not in my_dict)
# Output: False, because "a" is a key in the dictionary
print("d" not in my_dict)
# Output: True, because "d" is not a key in the dictionary

# Example with a range
my_range: range = range(1, 10)
print(5 not in my_range)
# Output: False, because 5 is present in the range
print(15 not in my_range)
# Output: True, because 15 is not present in the range
