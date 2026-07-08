# Local variables

# Local variables are only visible within the function in which they are
# defined.
# They are not available outside of that function.

def add_two_numbers() -> None:
    """ Add two numbers
        Args:
            None
        Returns:
            None
        Example:
            >>> add_two_numbers()
            4
    """
    a: int = 1  # local to function
    b: int = 3  # local to function
    print(a+b)


add_two_numbers()  # Prints 4
