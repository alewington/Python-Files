# XAND Truth Table

# The XAND operator (or not ^) is a logical operator that returns True if both
# operands are the same, and False if exactly one of the operands is True.
# The truth table for the XAND operator is as follows:

# A     B     A XAND B
# True  True  True
# True  False False
# False True  False
# False False True

# Example of using the XAND operator in Python
print(True ^ True)  # True
print(True ^ False)  # False
print(False ^ True)  # False
print(False ^ False)  # True

# The XAND operator is also known as the not-equal to (NE) operator.
# It can be used in an if statement to check whether two values are equal
# or not:
a: bool = True
b: bool = False

if a != b:
    print("a and b are not equal")
else:
    print("a and b are equal")

# The result is "a and b are not equal" because a is True and b is False, so
# they are not equal. The XAND operator can also be used in a while loop to
# check whether two values are equal or not:
while a != b:
    print("a and b are not equal")
    break
else:
    print("a and b are equal")
