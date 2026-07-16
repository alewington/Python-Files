# Non Local Variables

# Non local variables are variables that are not local to a function, but
# are defined outside of a function, but are used inside a nested function.


def function_one() -> None:
    x: int = 1  # local to this function.

    def function_two() -> None:
        nonlocal x  # non local variable, inline to x of function_one().
        x = x  # so it can be used in this scope.
        y = x + 10
        print(y)


# Calling the functions <EOT>
    function_two()
    print(x)


function_one()
