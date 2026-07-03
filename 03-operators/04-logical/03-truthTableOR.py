# OR Truth Table

# The OR operator (or) is a logical operator that returns True if at least one
# of the operands is True, and False if both operands are False. It is used to
# combine two or more conditions in a logical expression.
# The truth table for the OR operator is as follows:

# A     B     A OR B
# True  True  True
# True  False True
# False True  True
# False False False

# Example of using the OR operator in Python

print(True or True)  # Output: True (at least one of True or True needs
# to be True)
print(True or False)  # Output: True (at least one of True or False needs
# to be True)
print(False or True)  # Output: True (at least one of False or True needs
# to be True)
print(False or False)  # Output: False (both False and False need to be True

# for the result to be True)

# The OR operator is often used in conditional statements to check if at least
# one condition is met before executing a block of code.
# Example of using the OR operator in an if statement

is_weekend: bool = True
is_sunny: bool = False
if is_weekend or is_sunny:
    print("Let's go to the beach!")
    # Output: Let's go to the beach! (This will be printed because is_weekend
    # is True)
else:
    print("Maybe we can go to the park instead.")
    # Output: (This will not be printed because is_weekend is True)

# What is the answer to the above expression?
# True or False

# The answer is True because at least one of the conditions is True.
# Remember that the OR operator returns True if at least one operand is True,
# and False only if both operands are False.

# In summary, becareful which operator you choose. it may be the weekend
# but is the weather nice enough to go to the beach?
# if you use AND then you will only go to the beach if both
# conditions are True,
# but if you use OR then you will go to the beach if at least one of the
# conditions is True.
