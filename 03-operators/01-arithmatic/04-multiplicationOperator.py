# Multipplication Operator

# The multiplication operator *  multiplies two numbers together.

# For example:
print(3*2)  # prints 6

# other examples
print(5*7)  # prints 35

# The multiplication operator can be used with decimals too.
print(10.5*4)  # prints 42.0

# The multiplication operator can also be used to multiply strings together.
print("Hello " * 3)  # prints Hello Hello Hello

# The multiplication operator can also be used to repeat a string a number of
# times.
print("Hello" * 5)  # prints HelloHelloHelloHelloHello

# An example to use symbles to create seperators:
print("-"*70)
# output: ----------------...and so on up to 70 "-"

# The multiplication operator can also be used to repeat a list a number of
# times.
my_list = [1, 2, 3]
print(my_list*4)  # prints [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]


# The multiplication operator can also be used to repeat a tuple a number of
# times.
my_tuple = (1, 2, 3)
print(my_tuple*4)  # prints (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)

# The multiplication operator can also be used to repeat a bytearray a number
# of times.
my_bytearray = bytearray([1, 2,  3])
print(my_bytearray*4)  # prints bytearray(b'\\x01\\x02\\x03\\x01\\x02\\x03
# \\x01\\x02\\x03\\x01\\x02\\x03')

# The multiplication operator can also be used to repeat a bytearray a number
# of times.
my_bytes = bytes([1, 2, 3])
print(my_bytes*4)  # prints b'\\x01\\x02\\x03\\x01\\x02\\x03\\x01\\x02\\x03\\
# x01\\x02\\x03\\x01\\x02\\x03'

# The multiplication operator can also be used to repeat a complex number
# a number of times.
my_complex = 5+6j
print(my_complex*4)  # prints (25+24j)

# The multiplication operator can also be used to repeat a range a number
# of times.
for my_range in range(5, 10):
    print(my_range*4)  # prints 20, 24, 28, 32, 36
