# Things you can use the Addition Operator For

# You can add two numbers together to get their sum.
print(5 + 4)  # Prints 9

# or

# this loop demonstrates putting addition into functions.
for i in range(1, 11, 1):
    print(i, "+ 5 = ", 5 + i)

# These are more contatenated uses but useful when comparing later
# e.g.
test: str = "hello" + "world"
print(test == "helloworld")  # output: True

# You can also add a number and a string together.
# The result is the string with the number added in front of it.
print("Hello" + " World")  # Prints Hello World

# You can use addition to combine strings.
print("Hello" + " " + "World")  # Prints Hello World

# You can also add a string and an integer together.
# The result is the string with the number added at the end of it.
print("Hello" + str(4))  # Prints Hello4

# You can use addition to combine strings and integers.
print(str(100) + " bottles of beer on the wall")  # Prints 100 bottles of beer
# on the wall

# You can also add a string and a float together.
# The result is the string with the number added at the end of it.
print("Hello " + str(4.5))  # Prints Hello 4.5

# You can use addition to combine strings and floats.
print(str(10.5) + " pies on the wall")  # Prints 10.5 pies on the wall

# You can also add a string and a boolean together.
# The result is the string with the number added at the end of it.
print("Hello " + str(True))  # Prints Hello True

# You can use addition to combine strings and booleans.
print("it is all " + str(True))  # Prints it is all True
