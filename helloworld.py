print("Hello, World!")


def greeting(name):
    """
    Returns a greeting message for the given name.
    Args:
        name (str): The name of the person to greet.
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    name: str = input("Enter your name: ")
    print(greeting(name))
# This is a simple Python script that prints "Hello, World!".
# defines a function.
# using pep8 and flake8 style guidelines for better readability and maintain.
