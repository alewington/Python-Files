# User Input

# input() function is used to take input from the user.
# It always returns a string.
# name = input("Enter your name: ")
# print("Hello, " + name + "!")

name: str = input("Enter your name: ")
print(name)

# To take numerical input, we need to convert the
# string to the desired data type using int()
# or float() functions.

age: int = int(input("Enter your age: "))
print(age)

# Did you notice the casting of int? line 15.
# Just demoing that you can change the data type of the input of data.
