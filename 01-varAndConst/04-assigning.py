# Assigning multiple Variables at once

# Many to Many
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# One to Many
a: int = 1
b: int = 1
c: int = 1
print(a)
print(b)
print(c)

# expand a list into multiple variables
apples: list[str] = ["apple", "golden apple", "enchanted golden apple"]
apple1, apple2, apple3 = apples
print(apple1)
print(apple2)
print(apple3)

# use of the * operator to assign the rest of the values to a variable
name: list[str] = ["Albus", "Percival", "Wulfric", "Brian", "Dumbledore"]
first, *middle, last = name
print(first)
print(middle)
print(last)

# The *middle variable will be a list containing all the values in between the
# first and last values. In this case, it will contain
# ["Percival", "Wulfric", "Brian"].
# In this case it allows you to unpack a list into multiple variables,
# while also capturing any remaining values in a separate variable.

# Now you can use the variables as needed in your code. For example,
# you could print them out or use them in calculations.
print(f"Professor {first} {last} is a character from the Harry Potter series.")

print(
    f"The middle names are: {middle[0]}, {middle[1]}, and {middle[2]},",
    "which are also part of the character's full name.")

# *_ is frequently used to indicate that the variable is intentionally being
# ignored and not used.
# Example:
first, *_ = name
print(first)
