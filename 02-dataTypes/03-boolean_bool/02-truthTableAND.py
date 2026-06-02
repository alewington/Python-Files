# AND Truthtable

# The AND operator (&&) is a logical operator that returns True if both
# operands are True, and False otherwise. It is used to combine two or more
# conditions in a logical expression.
# The truth table for the AND operator is as follows:
# A     B     A AND B
# True  True  True
# True  False False
# False True  False
# False False False
# Example of using the AND operator in Python

print(True and True)  # Output: True (both True and True need to be True)
print(True and False)  # Output: False (both True and False need to be True)
print(False and True)  # Output: False (both False and True need to be True)
print(False and False)  # Output: False (both False and False need to be True)

# The AND operator is often used in conditional statements to check if
# multiple conditions are met before executing a block of code.

# Example of using the AND operator in an if statement

is_weekend = True
is_sunny = False

if is_weekend and is_sunny:
    print("Let's go to the beach!")
    # Output: (This will not be printed because is_sunny is False)
else:
    print("Maybe we can go to the park instead.")
    # Output: Maybe we can go to the park instead.

# What is the answer to the above expression?
# True and False

# The answer is False because both conditions need to be True for the
# AND operator to return True.
# Since one of the conditions is False, the result is False.
# Remember that the AND operator requires both operands to be True for the
# result to be True.
# If either operand is False, the result will be False.
