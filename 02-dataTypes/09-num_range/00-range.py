# What is range

# Range is
# 1) A function that takes 1,  or 3 arguments
# 2) It returns an iterable object (a list)
# 3) The elements of the returned list are integers
# 4) The length of the list is determined by the number of elements between
# the first and last integer in the range
# 5) If a third argument is given, it is called 'step'
# 6) This argument tells how much to increase each element in the range

# Example:

range(0, 10)  # returns [0,1,2,3,4,5,6,7,8,9]
range(0, 10, 2)  # returns [0,2,4,6,8]

# The following is a list of all the functions in this module:

# 1. def range(start stop[, step])
#    Returns a list containing an arithmetic progression of integers.
#    start: int or float - first number in the sequence
#    stop: int or float - last number in the sequence
#    step: optional - default value is 1
#          This determines how much to increase each element in the range
#           If this argument is negative, the elements will be decreased
#           instead.
#    Returns: list

# example doing the 10x times table

for i in range(1, 11):
    print(i, "times 10 = ", i*10)

# Example of a 'step' argument

# This will print all even numbers between 1 and 20

for i in range(2, 21, 2):
    print("Even number:", i)

# Example of using the 'range' function to iterate through a string

# The following is an example of using the 'range' function to iterate through
# a string.
# In this case, we are iterating through the string "hello" and printing each
# letter on its own line.

for i in range(len("Hello")):
    print("letter at position", i, "is", "Hello"[i])

# Example of using the 'range' function to iterate through a list

# The following is an example of using the 'range' function to iterate throug
# a list.
# In this case, we are iterating through the list [10,20,30] and printing each
# element on its own line.

for i in range(len([10, 20, 30])):
    print("element at position", i, "is", [10, 20, 30][i])
