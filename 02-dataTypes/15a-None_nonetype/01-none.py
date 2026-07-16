# NoneType

# None is a special constant in Python that represents the absence of a value
# or a null value. It is an object of its own datatype, the NoneType.
# You can assign None to a variable to indicate that it has no value. It is
# often used to represent the default value of function arguments, or to
# indicate that a variable has not been initialized. In Python, None is a
# singleton, which means there is only one instance of None in the entire
# Python runtime. You can check if a variable is None by using the `is`
# operator.

# Here is an example:
my_variable: str | None = None
if my_variable is None:
    print("my_variable is None")
else:
    print("my_variable has a value")

# Output: my_variable is None
