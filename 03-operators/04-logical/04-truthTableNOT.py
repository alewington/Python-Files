# NOT Truth Table

# The NOT operator (not) is a logical operator that returns the opposite of
# the operand.
# It is used to negate a boolean value.
# The truth table for the NOT operator is as follows:

# A     not A
# True  False
# False True

# Example of using the NOT operator in Python

print(not True)   # Output: False (the opposite of True)
print(not False)  # Output: True (the opposite of False)

# The NOT operator is often used in conditional statements to check
# if a condition is not met.
# Example of using the NOT operator in an if statement

is_raining: bool = False
if not is_raining:
    print("Let's go for a walk!")
    # Output: Let's go for a walk! (This will be printed because is_raining
    # is False)
else:
    print("Maybe we can stay inside and read a book.")
    # Output: (This will not be printed because is_raining is False)

# What is the answer to the above expression?
# not True

# The answer is False because the NOT operator returns the opposite of the
# operand.
# Remember that the NOT operator returns True if the operand is False,
# and False if the operand is True.

# Ever been to the pantomine, and the audience shouts "He's behind you!"
# the hero says "he's not",
# audience shouts back "He is behind you!"
# and then the hero turns around to find the villain is actually behind them?
# That's the NOT operator in action, it negates the truth value of the
# statement.
