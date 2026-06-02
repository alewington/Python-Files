# Simple interger Maths

# Addition
print(3+5)  # prints 8

# Adding out side of the print statement.
addTwoNumbers = 25 + 35
print(addTwoNumbers)  # prints 60

# You can also add variables that hold integers
numAdd1 = 23
numAdd2 = 21
print(numAdd1 + numAdd2)  # prints 44

# Subtraction
print(10 - 4)  # prints 6

# You can also subtract variables that hold integers
numSub1 = 50
numSub2 = 20
print(numSub1 - numSub2)  # prints 30

# Multiplication
print(4 * 6)  # prints 24

# You can also multiply variables that hold integers
numMul1 = 7
numMul2 = 8
print(numMul1 * numMul2)  # prints 56

# Division
print(20 / 5)  # prints 4.0 because division always returns a float

# You can also divide variables that hold integers
numDiv1 = 100
numDiv2 = 4
print(numDiv1 / numDiv2)  # prints 25.0 because division always returns
# a float
# so...
answerDiv = numDiv1 / numDiv2
print(int(answerDiv))  # prints 25 because we are casting the float to an int.

# Bidmas stands for brackets, indices, division, multiplication, addition and
# subtraction.
# Also known as PEMDAS, BODMAS, BEDMAS, etc.

# It is the order of operations that Python follows when evaluating an
# expression.
# You can use brackets to change the order of operations.
print(3 + 5 * 2)  # prints 13 because multiplication is done before addition
print((3 + 5) * 2)  # prints 16 because the brackets change the order of
# operations and addition is done before multiplication.
