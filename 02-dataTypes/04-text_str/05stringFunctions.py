# String - Premade Functions

# Python provides a variety of built-in functions and methods that you can use
# to manipulate and work with strings. Here are some commonly used
# string functions:

# len() function to get the length of a string
str_example = "Hello, World!"
print(len(str_example))
# This will print 13 to the console, demonstrating that the len() function
# returns the number of characters in the string, including spaces
# and punctuation.

# str() function to convert other data types to a string
number = 42
str_number = str(number)
print(str_number)
# This will print "42" to the console, demonstrating that the str() function
# converts the integer 42 to a string.

# upper() method to convert a string to uppercase
print(str_example.upper())
# This will print "HELLO, WORLD!" to the console, demonstrating that the
# upper() method converts all characters in the string to uppercase.

# lower() method to convert a string to lowercase
print(str_example.lower())
# This will print "hello, world!" to the console, demonstrating that the
# lower() method converts all characters in the string to lowercase.

# strip() method to remove leading and trailing whitespace
str_with_whitespace = "   Hello, World!   "
print(str_with_whitespace.strip())
# This will print "Hello, World!" to the console, demonstrating that the
# strip() method removes the leading and trailing whitespace from
# the string.

# replace() method to replace a substring with another substring
print(str_example.replace("World", "Python"))
# This will print "Hello, Python!" to the console, demonstrating that the
# replace() method replaces the substring "World" with "Python"
# in the string.

# split() method to split a string into a list of substrings
print(str_example.split(", "))
# This will print ['Hello', 'World!'] to the console, demonstrating that
# the split method splits the string into a list of substrings based
# on the specified delimiter (in this case, ", ").

# join() method to join a list of strings into a single string
str_list = ["Hello", "World", "from", "Python"]
joined_str = " ".join(str_list)
print(joined_str)
# This will print "Hello World from Python" to the console, demonstrating that
# the join() method is used to concatenate the strings in the list with a space
# as the separator.

# find() method to find the index of the first occurrence of a substring
print(str_example.find("World"))
# This will print 7 to the console, demonstrating that the find() method
# returns the index of the first occurrence of the substring "World" in
# the string, which starts at index 7.

# count() method to count the number of occurrences of a substring
print(str_example.count("o"))
# This will print 2 to the console, demonstrating that the count() method
# returns the number of occurrences of the substring "o" in the string,
# which appears twice.

# isalpha() method to check if all characters in the string are alphabetic
print(str_example.isalpha())
# This will print False to the console, demonstrating that the isalpha()
# method returns False because the string contains spaces and punctuation,
# which are not alphabetic characters.

# isdigit() method to check if all characters in the string are digits
str_digits = "12345"
print(str_digits.isdigit())
# This will print True to the console, demonstrating that the isdigit() method
# returns True because all characters in the string are digits.

# isspace() method to check if all characters in the string are whitespace
str_whitespace = "   "
print(str_whitespace.isspace())
# This will print True to the console, demonstrating that the isspace() method
# returns True because all characters in the string are whitespace.

# startswith() method to check if a string starts with a specific substring
print(str_example.startswith("Hello"))
# This will print True to the console, demonstrating that the startswith()
# method returns True because the string starts with the substring "Hello".

# endswith() method to check if a string ends with a specific substring
print(str_example.endswith("!"))
# This will print True to the console, demonstrating that the endswith()
# method returns True because the string ends with the substring "!".

# For extended list go here:
# https://www.w3schools.com/python/python_strings_methods.asp
