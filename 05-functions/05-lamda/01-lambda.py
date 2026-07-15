# Lambda

# A lambda function is a small anonymous function that can take any number of
# arguments, but can only have one expression. It is often used for short,
# simple functions that are not reused elsewhere in the code.

# Example usage of a lambda function
add = lambda x, y: x + y
# it is recommended to use a normal function instead of a lambda function for
# better readability and maintainability.
print(add(5, 3))

# Lambda functions are often used in conjunction with built-in functions like
# map(), filter(), and sorted().
# The benefit is that they allow you to define a function in a single line,
# making the code more concise and readable.
# Example usage of lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# Example usage of lambda with filter()
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

# Example usage of lambda with sorted()
sorted_numbers = sorted(numbers, key=lambda x: -x)
print(sorted_numbers)  # Output: [5, 4, 3, 2, 1]

# Be careful when using lambda functions, as they can make the code less
# readable if overused or used in complex scenarios.
