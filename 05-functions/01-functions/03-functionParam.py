# Function Parameters

# Functions are very important and useful in programming.  with out them code
# will be extremely long, problematic and unreadable.
# So using them has a great many benefits, these include:
# Benefits of functions:
# - Reusable code
# - Easier to read
# - Less error prone
# - More readable
# - More maintainable

# A times table function
def times_table(number: int) -> None:
    """Times tables of a given number
    Args:
        number(int): The number to be used in times table (parameter)
    Return:
        None
    example:
        >>> times_table(5)
        1 X 5 = 5
    """
    print(f"\nThe {number} Times Table\n")
    for i in range(1, 10):
        print(f"{i} X {number} = {i * number}", end="\n")


# Call the function
times_table(int(input('Enter a number: ')))
# the entered value is the arguement from the input()
times_table(2)  # 2 is the arguement
times_table(7)  # 7 is the arguement

# Parameters are values that are passed into functions. These can be used to
# change the output of a function. The parameters are defined in the function
# definition and then used when calling the function. In this example we have
# one parameters, number. We use this as input for the timetable.
