# Map Function

# The map() function applies a given function to all items in an iterable
# (e.g. list) and returns a map object.
# Example usage of map()
def square(n):
    return n * n


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
