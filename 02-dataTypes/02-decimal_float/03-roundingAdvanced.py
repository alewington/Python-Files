# other rounding methods
from decimal import (
    ROUND_HALF_UP,
    ROUND_HALF_DOWN,
    ROUND_HALF_EVEN,
    ROUND_UP,
    ROUND_DOWN,
    Decimal
)

decimal_d: float = Decimal('1.235')
print(decimal_d.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
# Output: 1.24
print(decimal_d.quantize(Decimal('0.01'), rounding=ROUND_HALF_DOWN))
# Output: 1.23
print(decimal_d.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN))
# Output: 1.24
print(decimal_d.quantize(Decimal('0.01'), rounding=ROUND_UP))
# Output: 1.24
print(decimal_d.quantize(Decimal('0.01'), rounding=ROUND_DOWN))
# Output: 1.23

# Decimal quantize() method allows you to specify the rounding method to use
# when rounding a Decimal object to a specific number of decimal places.
# The rounding parameter can take one of the following values:
#
# ROUND_HALF_UP: Rounds to the nearest neighbor, rounding up if the number is
# exactly halfway between two possibilities.
# ROUND_HALF_DOWN: Rounds to the nearest neighbor, rounding down if the number
# is exactly halfway between two possibilities.
# ROUND_HALF_EVEN: Rounds to the nearest neighbor, rounding to the nearest
# even number if the number is exactly halfway between two possibilities.
# ROUND_UP: Rounds away from zero.
# ROUND_DOWN: Rounds towards zero.


# Bankers Rounding


print(round(decimal_d, 2))  # Output: 1.24 bankers rounding

print(round(decimal_d))  # Output: 1 bankers rounding


# Bankers rounding is typically used for financial calculations to
# minimize cumulative rounding errors. It rounds to the nearest
# even number when the number is exactly halfway between two
# possibilities. In this case, 1.235 is rounded to 1.24
# because 4 is an even number.
# If you want to round to the nearest integer, you can use
# the built-in round() function, which also uses bankers rounding
# by default.
