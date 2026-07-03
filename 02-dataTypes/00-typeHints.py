# Type Hints in Python

hot_day: bool = True

print(hot_day)  # Output: True

# Type hints are a way to indicate the expected data types of variables,
# function parameters, and return values in Python. They are not enforced
# at runtime but can be used by static type checkers, IDEs, and linters
# to catch potential type errors.

# Here's an example of how to use type hints in Python:


def greet(name: str) -> str:
    return f"Hello, {name}!"
# In this example, the function greet takes a parameter name of type str and
# returns a value of type str.


print(greet("Alice"))  # Output: Hello, Alice!

# You can also use type hints for variables:
age: int = 30
height: float = 175.2
print(age)  # Output: 30
print(height)  # Output: 175.2

# Type hints can also be used with more complex data types, such as lists and
# dictionaries:

from typing import List, Dict


names: List[str] = ["Alice", "Bob", "Charlie"]
ages: Dict[str, int] = {
                        "Alice": 30,
                        "Bob": 25,
                        "Charlie": 45,
                        "Dave": 50
                        }
print(names)  # Output: ['Alice', 'Bob', 'Charlie']

# Type hints can also be used with optional types using the Optional type from
# the typing module:

from typing import Optional


def get_age(name: str) -> Optional[int]:
    if name in ages:
        return ages[name]
    else:
        return None
