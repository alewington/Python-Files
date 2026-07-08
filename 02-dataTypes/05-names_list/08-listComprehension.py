# List Comprehension

# List comprehension is a way to create a list using an expression.
# The syntax of a list comprehension is as follows:
# [expression for item in iterable if condition]

# Example 1
# Create a list of numbers from 0 to 9
numbers: list[int] = [i for i in range(10)]
print(numbers)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 2
# Create a list of even numbers from 0 to 10
evenNumbers: list[int] = [i for i in range(10) if i % 2 == 0]
print(evenNumbers)
# Output: [0, 2, 4, 6, 8]

# list comprehension in a for loop
# Example 3
# Create a list of numbers from 1 to 5
text: str = "It is a beautiful day!"
vowels: list[str] = [i for i in text if i in 'aeiouAEIOU']
print(len(vowels))
print(vowels)

# Please don't use List comprehension if readability becomes difficult.
