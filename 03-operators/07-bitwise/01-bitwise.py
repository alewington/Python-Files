# Bitwise

# Bitwise operators are used to perform operations on binary representations
# of integers. They operate at the bit level, allowing for efficient
# manipulation of data.

# The following are the common bitwise operators in Python:

# 1. AND (&): Performs a bitwise AND operation. Each bit of the output
# is 1 if the corresponding bits of both operands are 1, otherwise it is 0.

# Bitwise AND Operation
a: int = 10  # 00001010
b: int = 4  # 00000100
c: int = a & b  # 00000000
print(c)  # Output: 0
print(bin(c))  # Output: 0b0

# 2. OR (|): Performs a bitwise OR operation. Each bit of the output is 1 if
# at least one of the corresponding bits of the operands is 1, otherwise
# it is 0.

# Bitwise OR Operation
d: int = a | b  # 00001110
print(d)  # Output: 14
print(bin(d))  # Output: 0b1110

# 3. XOR (^): Performs a bitwise XOR operation. Each bit of the output is 1
# if the corresponding bits of the operands are different, otherwise it is 0.

# Bitwise XOR Operation
e: int = a ^ b  # 00001110
print(e)  # Output: 14
print(bin(e))  # Output: 0b1110

# 4. NOT (~): Performs a bitwise NOT operation. It inverts the bits of the
# operand, changing 1s to 0s and 0s to 1s.

# Bitwise NOT Operation
f: int = ~a  # 11110101 (in two's complement representation)
print(f)  # Output: -11
print(bin(f))  # Output: -0b1011

# 5. Left Shift (<<): Shifts the bits of the first operand to the left by the
# number of positions specified by the second operand. This effectively
# multiplies the first operand by 2 raised to the power of the second operand.

# Left Shift Operation
g: int = a << 2  # 00101000
print(g)  # Output: 40
print(bin(g))  # Output: 0b101000

# 6. Right Shift (>>): Shifts the bits of the first operand to the right by
# the number of positions specified by the second operand. This effectively
# divides the first operand by 2 raised to the power of the second operand.

# Right Shift Operation
h: int = a >> 2  # 00000010
print(h)  # Output: 2
print(bin(h))  # Output: 0b10
