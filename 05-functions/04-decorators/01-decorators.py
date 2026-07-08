# decorators

# Decorators are functions that take a function as an argument and return
# another function.
def my_decorator(func):
    """decorator
    Args:
        func (function): function to be decorated
    Returns:
        function: decorated function
    Example:
        >>> @my_decorator
        ...     def say_whee():
        ...         print('whee!')
        >>> say_whee()
        Something is happening before the function is called.
        whee!
        Something is happening after the function is called.
    """
    def wrapper():
        """ adds something before and after say_whee()
        Args:
            func (function): function to be decorated
        Returns:
            function: decorated function
        Example:
            >>> @my_decorator
            ...     def say_whee():
            ...         print('whee!')
            >>> say_whee()
            Something is happening before the function is called.
            whee!
            Something is happening after the function is called.
        """
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Decorators can be used to modify a function without explicitly modifying it.


@my_decorator
def say_whee():
    """ print whee
    Args:
        None
    returns:
        None
    Example:
        >>> say_whee()
        Whee!
    """
    print("Whee!")


say_whee()

# The are used to add additional functionality to functions, such as logging or
# timing.
