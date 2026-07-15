# Generators

# A generator is a function that returns an iterator that produces a sequence
# of values when iterated over. Generators are defined using the `yield`
# statement, which allows the function to produce a value and pause its
# execution, resuming from where it left off when the next value is requested.

# It allows you to create iterators in a more concise and readable way
# compared to using classes and the `__iter__` and `__next__` methods.

# Also reduces memory usage since it generates values on-the-fly instead of
# storing them all in memory at once.
# Great for working with large datasets or infinite sequences.

def simple_generator():
    yield 1
    yield 2
    yield 3


# Example usage of the simple_generator
gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# Example usage of the simple_generator in a loop
for value in simple_generator():
    print(value)  # Output: 1, 2, 3


# Another example of a generator that produces an infinite sequence of
# Fibonacci numbers:
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Example usage of the fibonacci_generator
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
