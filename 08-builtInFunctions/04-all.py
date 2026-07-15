# All function

# The all() function returns True if all elements of an iterable are true (or
# if the iterable is empty).

# Example usage of all()
numbers = [1, 2, 3, 4, 5]
print(all(n > 0 for n in numbers))  # True

mixed = [1, 0, 3]
print(all(mixed))  # False
