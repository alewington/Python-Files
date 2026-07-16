# Type Hints in Python

hot_day: bool = True

print(hot_day)  # Output: True

# Type hints are a way to indicate the expected data types of variables,
# function parameters, and return values in Python. They are not enforced
# at runtime but can be used by static type checkers, IDEs, and linters
# to catch potential type errors.

# Here's an example of how to use type hints in Python:


def greet(name: str) -> str:
    """A function that takes a string and returns a greeting message.
    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.

    Examples:
        >>> greet("Alex")
        'Hello, Alex!'
    """
    return f"Hello, {name}!"
# In this example, the function greet takes a parameter name of type str and
# returns a value of type str.


print(greet("Alex"))  # Output: Hello, Alex!

# You can also use type hints for variables:
age: int = 30
height: float = 175.2
print(age)  # Output: 30
print(height)  # Output: 175.2
