# Strings

# A string is a sequence of characters.
# It can be defined using single quotes, double quotes, or
# triple quotes.
# Example of defining strings
str_text = 'Hello World!'
print(str_text)
# This will print "Hello World!" to the console


# Strings can also be defined using double quotes
str_text_double = "Hello World!"
print(str_text_double)
# This will also print "Hello World!" to the console

# Triple quotes can be used for multi-line strings
str_text_triple = """This is a multi-line string.
It can span multiple lines."""
print(str_text_triple)
# This will print the multi-line string as it is defined.

# Understanding that you can use diffent types is helpful for using them together.
str_text_mixed = 'Hello "World"!'
print(str_text_mixed)
# This will print 'Hello "World"!' to the console, demonstrating that you can use
# double quotes inside a string defined with single quotes without needing to escape them.
str_text_mixed2 = "Hello 'World'!"
print(str_text_mixed2)
# This will print "Hello 'World'!" to the console, demonstrating that you can use
# single quotes inside a string defined with double quotes without needing to escape them.

