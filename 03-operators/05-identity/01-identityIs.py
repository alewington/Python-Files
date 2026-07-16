# Identity IS

# The identity operator is used to compare the memory location of two objects.
# It checks whether two variables point to the same object in memory.
x: int = 5
y: int = 5
z: int = x

# Using the identity operator 'is' to compare x and y
print(x is y)  # Output: True, because both x and y point to the same integer
# object in memory (5)
# Using the identity operator 'is' to compare x and z
print(x is z)  # Output: True, because z is assigned the value of x
# Using the identity operator 'is' to compare y and z
print(y is z)  # Output: True, because both y and z point to the
# same integer object in memory (5)
