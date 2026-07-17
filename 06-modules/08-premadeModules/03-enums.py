# enums

# Enums are a way to define a set of named values. They can be used to
# represent a collection of related constants, making code more readable
# and maintainable.
# Enums are defined using the enum module.

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# Example usage of the Color enum
def print_color(color):
    """Prints the name of the color.
  Args:
        color (Color): An instance of the Color enum.
    Returns:
        None
    Raises:
        None
    Example:
        >>> print_color(Color.RED)
        The color is Red.
    """
    if color == Color.RED:
        print("The color is Red.")
    elif color == Color.GREEN:
        print("The color is Green.")
    elif color == Color.BLUE:
        print("The color is Blue.")
    else:
        print("Unknown color.")


# Testing the print_color function with different enum values
print_color(Color.RED)    # Output: The color is Red.
print_color(Color.GREEN)  # Output: The color is Green.

# Testing the print_color function with an unknown color
print_color(4)  # Output: Unknown color.

# Accessing enum members and their values
print(Color.RED)          # Output: Color.RED
print(Color.RED.name)     # Output: RED
print(Color.RED.value)    # Output: 1

# Iterating over enum members
for color in Color:
    print(f"{color.name} = {color.value}")

# Comparing enum members
print(Color.RED == Color.GREEN)  # Output: False
print(Color.RED == Color.RED)    # Output: True

# enums can also be used in switch-like statements using if-elif-else
# constructs, as shown in the print_color function. They provide a clear
# and structured way to handle a set of related constants, improving code
# clarity and reducing the likelihood of errors.
