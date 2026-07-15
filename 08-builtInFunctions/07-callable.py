# Callable Function

# Callable is a built-in function in Python that checks if an object appears
# to be callable (i.e., if it can be called as a function). It returns True
# if the object is callable, and False otherwise.

# Example usage of callable()
def my_function():
    return "Hello, World!"


print(callable(my_function))  # True
print(callable(42))           # False
