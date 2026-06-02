# Boolean or Bool

# A boolean is a data type that can only have two values:
# True or False. It is used to represent the truth value of an expression
# or a condition.
# In Python, you can create a boolean by using the keywords True and False.
# Example of creating a boolean about light switches or placing a block in
# minecraft

light_switch_on = True
print(light_switch_on)  # Output: True

block_placed = False
print(block_placed)  # Output: False

# You can also perform logical operations with booleans, such as AND, OR,
# and NOT.
# Example of logical operations with booleans

a = True
b = False
print(a and b)  # Output: False (both a and b need to be True)
print(a or b)   # Output: True (at least one of a or b needs to be True)
print(not a)    # Output: False (not True is False)
print(not b)    # Output: True (not False is True)

# Booleans are often used in conditional statements, such as if statements, to
# control the flow of a program based on certain conditions.
# Example of using booleans in an if statement

is_raining = True
if is_raining:
    print("Don't forget to take an umbrella!")
    # Output: Don't forget to take an umbrella!
else:
    print("Enjoy the sunshine!")

# More in section 03-operators/04-logical/
# all about logical operators and their truth tables.