# enums

# Enums are a way to define a set of named values. They can be used to
# represent a collection of related constants, making code more readable
# and maintainable.
# Enums are defined using the enum module.

from enum import Enum


class color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# Example usage of the color enum
def print_color(color):
    """Prints the name of the color.
  Args:
        color (color): An instance of the color enum.
    Returns:
        None
    Raises:
        None
    Example:
        >>> print_color(color.RED)
        The color is Red.
    """
    if color == color.RED:
        print("The color is Red.")
    elif color == color.GREEN:
        print("The color is Green.")
    elif color == color.BLUE:
        print("The color is Blue.")
    else:
        print("Unknown color.")


# Testing the print_color function with different enum values
print_color(color.RED)    # Output: The color is Red.
print_color(color.GREEN)  # Output: The color is Green.

# Testing the print_color function with an unknown color
# print_color(4)  # Output: Unknown color.

# Accessing enum members and their values
print(color.RED)          # Output: color.RED
print(color.RED.name)     # Output: RED
print(color.RED.value)    # Output: 1

# Iterating over enum members
for c in color:
    print(f"{c.name} = {c.value}")

# Comparing enum members
print(color.RED == color.GREEN)  # Output: False
print(color.RED == color.RED)    # Output: True

# enums can also be used in switch-like statements using if-elif-else
# constructs, as shown in the print_color function. They provide a clear
# and structured way to handle a set of related constants, improving code
# clarity and reducing the likelihood of errors.
