# Args

# Args are positional arguments, which means that they must be passed in a
# specific order.


def add_it_all(*a: int) -> None:
    """add two or more integers together with *args

    Args:
        a (int): integer value of number one to add
        b (int): integer value of number two to add

    Returns:
        None

    Example:
        >>> add_it_all(1, 2)
        3
    """
    print(a)
    total = 0
    for numbers in a:
        total = numbers + total
    print(total)


print(add_it_all(1, 2, 3, 4))  # 10

# Example
# def people_hello(*people: str, message: str="hello"):") -> None
