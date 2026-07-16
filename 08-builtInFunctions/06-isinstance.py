# isinstance

# The isinstance() function is used to check if an object is an instance of a
# specified class or a subclass thereof. It returns True if the object is an
# instance of the class or a subclass, and False otherwise.

# Example usage of isinstance()
x: int = 10
print(isinstance(x, int))  # True
print(isinstance(x, str))  # False

# You can also check for multiple types by passing a tuple of types
y: float = 3.14
print(isinstance(y, (int, float)))  # True


# Checking for a subclass
class Animal:
    pass


class Dog(Animal):
    pass


print(isinstance(Dog(), Animal))  # True
