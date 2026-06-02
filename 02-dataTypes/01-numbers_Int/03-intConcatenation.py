# Concatenation with Integers

# Using "+" operator

# Concatenation is the operation of joining two strings together. In Python,
# you can concatenate strings using the `+` operator. However, when you try to
# concatenate an integer with a
# string, you will encounter a TypeError because they are different data types.
# For example:
num = 10
text = "The number is: "
# This will raise a TypeError because you cannot concatenate a string and an
# integer
# print(text + num)
# To concatenate an integer with a string, you need to convert the integer to
# a string using the `str()` function. For example:
print(text + str(num))  # prints "The number is: 10"

# Dangers of "+" Operator for concatenation
# While the `+` operator can be used for concatenation, it can lead to
# unexpected results if you are not careful. For example, if you have two
# integers and you use the `+` operator, it will perform addition instead of
# concatenation. For example:
num1 = 5
num2 = 10
print(num1 + num2)  # prints 15 because it performs addition instead of
# concatenation.
print(str(num1) + str(num2))  # prints "510" because it concatenates the
# two integers as strings.
# This is why it is important to be aware of the data types you are working
# with and to use the appropriate method for concatenation.

##############################################################################

# Using "," operator

# Another method is to use the "," operator in the print function, which
# automatically converts the integer to a string and adds a space between the
# string and the integer. For example:
print(text, num)  # prints "The number is: 10" with a space between the string
# and the integer.
# This method is often preferred for printing multiple items because it is
# more concise and automatically handles the conversion of different
# data types to strings.

###############################################################################

# Using f-strings

# Alternatively, you can use an f-string to concatenate the integer with the
# string. For example:
print(f"{text}{num}")  # prints "The number is: 10"
# Both of these methods will allow you to concatenate an integer with a string
# without raising a Type Error.
