# To mitigate precision issues, you can use the decimal module in Python,
# which provides a Decimal data type for decimal floating-point arithmetic.
from decimal import Decimal

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
