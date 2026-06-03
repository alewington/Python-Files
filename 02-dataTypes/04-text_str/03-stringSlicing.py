# String Slicing

# String slicing allows you to extract a portion of a string by specifying
# a range of indices. The syntax for slicing is:
# string[start:stop:step]
# - start: The index where the slice starts (inclusive). If omitted, it
# defaults to the beginning of the string (index 0).
# - stop: The index where the slice ends (exclusive). If omitted, it defaults
# to the end of the string.
# - step: The step size or stride between characters in the slice.
# If omitted, it defaults to 1.
str_text = "Hello World!"
# Example of slicing a string
print(str_text[0:5])
# This will print "Hello" to the console, demonstrating that the slice
# starts at index 0 and ends at index 5 (exclusive), resulting in "Hello".
print(str_text[6:11])
# This will print "World" to the console, demonstrating that the slice
# starts at index 6 and ends at index 11 (exclusive), resulting in "World
# The step parameter can be used to skip characters in the slice
print(str_text[0:12:2])
# This will print "HloWrd" to the console, demonstrating that the slice
# starts at index 0, ends at index 12 (exclusive), and includes every second
# character, resulting in "HloWrd".
print(str_text[::3])
# This will print "Hl r!" to the console, demonstrating that the slice
# includes every third character from the entire string, resulting in "Hl r!".
print(str_text[::-1])
# This will print "!dlroW olleH" to the console, demonstrating that the
# slice includes every character in reverse order, resulting in the reversed
# string "!dlroW olleH".

# Concatenation and repetition with slices
print(str_text[0:5] + " " + str_text[6:11])
# This will print "Hello World" to the console, demonstrating that you can
# concatenate slices of a string using the + operator to create a new string.
print(str_text[0:5] * 2)
# This will print "HelloHello" to the console, demonstrating that you can
# repeat a slice of a string using the * operator to create a new string.
print(str_text[0:5] + " " + str_text[6:11] + " " + str_text[0:5] * 2)
# This will print "Hello World HelloHello" to the console, demonstrating that
# you can combine slicing with operators to create more complex strings.
print(str_text[0:5], str_text[6:11])
# This will print "Hello World" to the console, demonstrating that you can
# use the print function to print multiple slices of a string separated by a
# space by default.

# Comparison of slices
print(str_text[0:5] == str_text[6:11])
# This will print False to the console, demonstrating that the slice "Hello"
# is not equal to the slice "World", resulting in False.
print(str_text[0:5] != str_text[6:11])
# This will print True to the console, demonstrating that the slice "Hello"
# is not equal to the slice "World", resulting in True.
