# XOR Truth Table

# The XOR operator (or ^) is a logical operator that returns True if
# exactly one of the operands is True, and False if both operands
# are the same.
# The truth table for the XOR operator is as follows:

# A     B     A XOR B
# True  True  False
# True  False True
# False True  True
# False False False

# Example of using the XOR operator in Python

print(True ^ True)  # Output: False (both operands are True)
print(True ^ False)  # Output: True (only one operand is True)
print(False ^ True)  # Output: True (only one operand is True)
print(False ^ False)  # Output: False (both operands are False)

# The XOR operator is often used in conditional statements to check if
# exactly one condition is met before executing a block of code.
# Example of using the XOR operator in an if statement

is_weekend = True
is_sunny = False
if is_weekend ^ is_sunny:
    print("Let's go to the beach!")
    # Output: Let's go to the beach! (This will be printed because exactly
    # one of is_weekend or is_sunny is True)
else:
    print("Maybe we can go to the park instead.")
    # Output: (This will not be printed because both conditions are not met)

# What is the answer to the above expression?
# True ^ False

# The answer is True because exactly one of the conditions is True.
# Remember that the XOR operator returns True if exactly one operand is True,
# and False if both operands are the same.
