# Identity IS NOT

# The identity operator 'is not' is used to compare the memory location of
# two objects.
# It checks whether two variables do not point to the same object in memory.
a: int = 10
b: int = 20
c: int = a

# Using the identity operator 'is not' to compare a and b
print(a is not b)  # Output: True, because a and b point to different
# integer objects in memory (10 and 20)
# Using the identity operator 'is not' to compare a and c
print(a is not c)  # Output: False, because c is assigned the value of
# a, so they point to the same integer object in memory (10)
# Using the identity operator 'is not' to compare b and c
print(b is not c)  # Output: True, because b and c point to different
# integer objects in memory (20 and 10)
