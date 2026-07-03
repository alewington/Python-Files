# Evaluating statements with boolean values
# True and False are reserved words in Python, so they cannot be used
# as variable names
# They are used to represent the truth value of an expression

# Example of a boolean expression
print(10 > 5)  # This will print True because 10 is greater than 5
print(10 < 5)  # This will print False because 10 is not less than 5
print(10 == 10)  # This will print True because 10 is equal to
print(10 != 5)  # This will print True because 10 is not equal to 5
print(10 >= 10)  # This will print True because 10 is greater than or
# equal to 10

# Boolean values can also be used in conditional statements
if 10 > 5:
    print("10 is greater than 5")
    # This will be executed because the condition is True
if 10 < 5:
    print("10 is less than 5")
    # This will not be executed because the condition is False
if 10 == 10:
    print("10 is equal to 10")
    # This will be executed because the condition is True
if 10 != 5:
    print("10 is not equal to 5")
    # This will be executed because the condition is True
if 10 >= 10:
    print("10 is greater than or equal to 10")
    # This will be executed because the condition is True


# Boolean values can also be used to compare strings
a: str = "Squirtle"
b = "Charmander"

print(a == b)
# This will print False because "Squirtle" is not equal to "Charmander"
print(a != b)
# This will print True because "Squirtle" is not equal to "Charmander"


# Evaluation of boolean values
print(bool())
# This will print False because an empty string is considered False
print(bool(15))
# This will print True because any non-zero number is considered True
print(bool(0))
# This will print False because 0 is considered False
print(bool(""))
# This will print False because an empty string is considered False
print(bool("Hello"))
# This will print True because a non-empty string is considered True
print(bool([]))
# This will print False because an empty list is considered False
print(bool([1, 2, 3]))
# This will print True because a non-empty list is considered True
print(bool(None))
# This will print False because None is considered False
