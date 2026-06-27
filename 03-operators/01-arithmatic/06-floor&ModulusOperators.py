# Floor and Modulus Operators:

# THe Floor Operator (//) returns the integer quotient of two numbers.
print(5 // 2)  # 2

# The Modulus Operator (%) returns the remainder of a division operation.
print(5 % 2)  # 1


# so
a = 3
b = 9

# The Floor Operator (//) returns the integer quotient of two numbers.
print(b // a)  # 3

# The Modulus Operator (%) returns the remainder of a division operation.
print(b % a)  # 0

print("the quotient is", b // a, "and remainder is", b % a)

# # The Floor and Modulus operators can be used together to find the
# greatest common divisor of two numbers:
a = 30
b = 40
while b != 0:
    old_b = b
    b = a % b
    a = old_b
print(a)  # 10

# The Floor and Modulus operators can be used together to find the
# least common multiple of two numbers:
a = 30
b = 40
while b != 0:
    old_b = b
    b = a % b
    a = old_b
print(a * (40 // 10))  # 120
