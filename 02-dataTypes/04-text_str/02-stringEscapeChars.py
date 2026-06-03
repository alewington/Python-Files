# String - Escape Characters

# Understanding that you can use different types of quotes to define strings
# is helpful, but sometimes you may want to use the same type of quote within
# a string. In such cases, you can use escape characters to include special
# characters in your strings.
# An escape character is a backslash (\) followed by the character you want to
# include in the string.

# \' for single quotes
str_with_quote = 'It\'s a nice day!'
print(str_with_quote)
# This will print "It's a nice day!" to the console, demonstrating that the
# single quote

# \" for double quotes
# is included in the string by escaping it with a backslash.
str_with_double_quote = "She said, \"Hello!\""
print(str_with_double_quote)
# This will print 'She said, "Hello!"' to the console, demonstrating that the
# double quotes are included in the string by escaping them with a backslash.

# \n for new line
# Escape characters can also be used for other special characters, such as
# newlines (\n) and tabs (\t).
str_with_newline = "Hello\nWorld!"
print(str_with_newline)
# This will print:
# Hello
# World!
# demonstrating that the \n creates a new line in the string.

# \t for tab space
str_with_tab = "Hello\tWorld!"
print(str_with_tab)
# This will print "Hello    World!" to the console, demonstrating that the
# \t creates a tab space between "Hello" and "World!" in the string.

# \\ for backslash
str_with_backslash = "This is a backslash: \\"
print(str_with_backslash)
# This will print "This is a backslash: \" to the console, demonstrating that
# the double backslash (\\) is used to include a single backslash in the
# string.

# \r for carriage return
str_with_carriage_return = "Hello\rWorld!"
print(str_with_carriage_return)
# This will print "World!" to the console, demonstrating that the \r carriage
# return moves the cursor back to the beginning of the line, allowing "World!"
# to overwrite "Hello".

# \b for backspace
str_with_backspace = "Hello\bWorld!"
print(str_with_backspace)
# This will print "HellWorld!" to the console, demonstrating that
# the \b backspace removes the character before it, resulting in
# "HellWorld!" instead of "HelloWorld!".


# \f for form feed - advanced
str_with_form_feed = "Hello\fWorld!"
print(str_with_form_feed)
# This will print "Hello" followed by a form feed (which may not be visible in
# the console) and then "World!", demonstrating that the \f form feed creates
# a page break in the string.

# \ooo for octal value - advanced
str_with_octal = "This is an octal character: \101"
print(str_with_octal)
# This will print "This is an octal character: A" to the console, demonstrating
# that the \ooo escape sequence allows you to include a character based on its
# octal value (in this case, \101 represents the letter 'A').

# \xhh for hexadecimal value - advanced
str_with_hex = "This is a hexadecimal character: \x41"
print(str_with_hex)
# This will print "This is a hexadecimal character: A" to the console,
# demonstrating that the \xhh escape sequence allows you to include a
# character based on its hexadecimal value
# (in this case, \x41 represents the letter 'A').
