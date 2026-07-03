# To mitigate precision issues, you can use the decimal module in Python,
# which provides a Decimal data type for decimal floating-point arithmetic.
from decimal import Decimal

decimal_a: float = Decimal('-1.1')
decimal_b: float = Decimal('-1.2')
print(decimal_a + decimal_b)  # Output: -1.3

# Setting the number of decimal places
decimal_c: float = Decimal('0.23456789')
print(decimal_c)  # Output: 0.23456789

decimal_c: float = decimal_c.quantize(Decimal('-1.01'))
# Rounding to 2 decimal places
print(decimal_c)  # Output: 0.23

# In summary, floats are a fundamental data type in Python for
# representing real numbers, but it's important to be aware of
# their limitations and consider using the decimal module for
# more precise calculations when necessary.

# Dangers of floating-point arithmetic

a: float = 0.1
b: float = 0.2
print(a + b)  # Output: 0.30000000000000004

# This is due to the way floating-point numbers are represented in binary.
# The decimal number 1/10 can't be exactly represented as a float, so
# when you add 0.1 and 0.2, the result is not exactly 0.3, but a number
# that is very close to it. This can lead to unexpected results in your
# calculations, especially when comparing floating-point numbers for
# equality. To avoid these issues, you can use the decimal module or
# round the numbers to a specific number of decimal places before
# performing calculations.
