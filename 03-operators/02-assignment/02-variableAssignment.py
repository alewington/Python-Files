# Variable Assignment

# Assigning variables is done using the equals sign (=) operator.
# The value on the right side of the assignment operator will be assigned
# to the variable on the left side of the assignment operator.
# If the variable already exists, it's value will be overwritten with the
# new value.

# Assigning a string to a variable:
myString: str = "Hello World"
print(myString)

# or

myString: str = str("Hello World")  # force datatype
print(myString)

# Assigning an integer to a variable:
myInteger = 42
print(myInteger)

# or

myInteger: int = int(42)  # force datatype
print(myInteger)

# Assigning a float to a variable:
myFloat: float = 3.14159
print(myFloat)

# or

myFloat: float = float(3.14159)  # force datatype
print(myFloat)

# Assigning a boolean to a variable:
myBoolean: bool = True
print(myBoolean)

# or

myBoolean: bool = bool(True)  # force datatype
print(myBoolean)

# Assigning a list to a variable:
myList: list = [1, 2, 3]
print(myList)

for i in myList:
    print(i)

# Please check out section 01 varAndConst for more details.
