# main() function

# main() function is used to run the program.
# It is a special function that is called when the program starts.
# The main() function can be defined in any module, but it must be called from
# the main module. The main() function should return an integer value.

# It reduces name shadowing and avoids confusion.

def minecraft_list(peops: list[str]) -> None:
    """Prints a greeting to each person in the list.
    Args:
        peops (list[str]): _description_
    Returns:
        None
    Example:
        >>> minecraft_list(['Steve', 'Alex', 'Villager335'])
        Hello, Steve!
    """
    for person in peops:
        print(f'Hello, {person}!')


def main() -> None:
    """Main function.
    Args:
        None
    Returns:
        None
    Example:
        >>> main()
        Hello, Steve!
    """
    peops: list[str] = ['steve', 'Alex', 'Villager335']
    minecraft_list(peops)


if __name__ == '__main__':
    main()
