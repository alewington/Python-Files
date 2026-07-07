# Decorator

def layout_decorator(func):
    def wrapper(x):
        print("_"*40)
        func(x)
        print("_"*40)
        return x
    return wrapper


@layout_decorator
def times_tables(number: int) -> None:
    number = int(5)
    for i in range(1, 10):
        print(f"{i} * {number} = {i*number}")


times_tables(3)
times_tables(7)
