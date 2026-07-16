print("Hello, World!")


def greeting(name: str) -> str:
    """Returns a greeting message for the given name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.

    Examples:
        >>> greeting("Steve")
        'Hello, Steve!'
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    name: str = input("Enter your name: ")
    print(greeting(name))

# This is a simple Python script that prints "Hello, World!".
# defines a function.
# The function takes a string argument (name) and returns a greeting message.
# The docstring describes the function's behavior in detail.
# The script also includes a main block that prompts the user for their name
# and prints a personalized greeting using the greeting function.
# The __main__ conditional statement ensures that the code is only run when
# the script is executed directly, not when it is imported as a module.
