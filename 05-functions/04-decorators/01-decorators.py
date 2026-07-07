# decorators

# Decorators are functions that take a function as an argument and return
# another function.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Decorators can be used to modify a function without explicitly modifying it.


@my_decorator
def say_whee():
    print("Whee!")


say_whee()

# The are used to add additional functionality to functions, such as logging or
# timing.
