# integer

# integer refer to whole numbers like 1, 5, 10 , 1,000, -2, 1,000,000,000
# As long as you have enough memory you can store as big and as many integers
# to fill it up in Python 3.

# Assigning integers
numInt = 100

print(numInt)  # prints 100 defaults as int
print(type(numInt))  # prints <class 'int'>


# casting to int
numInt2 = int(1.59)  # float to int
print(numInt2)  # prints 1
print(type(numInt2))  # prints <class 'int'>


# please note this is NOT rounding, it just removes the decimal part and keeps
# the whole number part.
# this will be covered later.

# Did you know?

# You can also assign integers with underscores to make them more readable
numInt2 = 1_000_000
print(numInt2)  # prints 1000000
print(type(numInt2))  # prints <class 'int'>
