# Float

# A float is a number that has a decimal point. It can be used to represent
# real numbers, such as 3.14 or -0.001.
# In Python, you can create a float by using a decimal point or by using
# scientific notation.

# Example of creating a float using a decimal point
pi = 3.14
print(pi)  # Output: 3.14

# Example of creating a float using scientific notation
avogadro_number = 6.022e23
print(avogadro_number)  # Output: 6.022e+23

# You can also perform arithmetic operations with floats,
# such as addition, subtraction, multiplication, and division.
a = 1.5
b = 2.5
print(a + b)  # Output: 4.0
print(a - b)  # Output: -1.0
print(a * b)  # Output: 3.75
print(a / b)  # Output: 0.6
# It's important to note that floats can sometimes lead to precision
# issues due to the way they are represented in memory.
# For example, the result of 0.1 + 0.2 may
# not be exactly 0.3 due to floating-point arithmetic.
print(0.1 + 0.2)  # Output: 0.300

# Don't forget the principles of BIDMAS when performing operations with floats
# , which stands for Brackets, Indices, Division and Multiplication
# (from left to right), Addition and Subtraction (from left to right).
result = (1.5 + 2.5) * 3 - 4 / 2
print(result)  # Output: 11.0
