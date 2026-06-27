# Exponentiation operator

# The eponentiation operator is the ** character. It raises a number
# to a power.
print(2**4)  # 16

# You can use it with any numeric type, including floats and complex numbers:
print((3+4j)**2)  # (-7j+24)

# The exponentiation operator is right associative, so you can
# write a ** b ** c as a ** b * c.
print(2**3**2)  # 512

# You can use negative exponents to calculate reciprocals:
print(4**-1)  # 0.25

# The exponentiation operator is not limited to integer powers, you can
# also use it with fractions:
print(3**(1/2))  # 1.7320508075688772

# You can also use negative exponents for fractional powers:
print(4**(-1/2))  # 0.5 + 0.8660254037844386j
