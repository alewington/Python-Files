# Filter Function

# The filter() function constructs an iterator from elements of an iterable
# for which a function returns true.
# Example usage of filter()
def is_even(n):
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]
