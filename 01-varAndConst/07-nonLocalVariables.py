# Non Local Variables

def function_one() -> None:
    x: int = 1

    def function_two() -> None:
        nonlocal x  # non local variable, inline to x.
        x = x  # so it can be used in this scope.
        y = x + 10
        print(y)


# Calling the functions <EOT>
    function_two()
    print(x)


function_one()
