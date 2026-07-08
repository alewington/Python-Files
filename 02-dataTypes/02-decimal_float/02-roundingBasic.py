# To mitigate precision issues, you can use the decimal module in Python,
# which provides a Decimal data type for decimal floating-point arithmetic.
from decimal import Decimal

# If using Decimal you don't need :float as the type for numbers. This is due
# to the fact that Decimal is a subclass of float.
# You can convert Dceimal to float if you wish.
# Decimal is more accurate to float but requires the module to be imported.

decimal_a = Decimal('-1.1')
decimal_b = Decimal('-1.2')
print(decimal_a + decimal_b)  # Output: -1.3

# Setting the number of decimal places
decimal_c = Decimal('0.23456789')
print(decimal_c)  # Output: 0.23456789

decimal_c = decimal_c.quantize(Decimal('-1.01'))
# Rounding to 2 decimal places
print(decimal_c)  # Output: 0.23

# In summary, floats are a fundamental data type in Python for
# representing real numbers, but it's important to be aware of
# their limitations and consider using the decimal module for
# more precise calculations when necessary.

# Dangers of floating-point arithmetic

a: float = 0.1
b: float = 0.2
print(f'float: {a + b}')  # Output: 0.30000000000000004

# This is due to the way floating-point numbers are represented in binary.
# The decimal number 1/10 can't be exactly represented as a float, so
# when you add 0.1 and 0.2, the result is not exactly 0.3, but a number
# that is very close to it. This can lead to unexpected results in your
# calculations, especially when comparing floating-point numbers for
# equality. To avoid these issues, you can use the decimal module or
# round the numbers to a specific number of decimal places before
# performing calculations. All because of how floating point numbers
# are stored in memory.

c = Decimal('0.1')
d = Decimal('0.2')
print(f'Decimal: {c + d}')  # Output: 0.3
