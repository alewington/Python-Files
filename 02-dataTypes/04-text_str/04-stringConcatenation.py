# Concatenation

# String concatenation is the process of combining two or more strings into a
# single string. In Python, you can concatenate strings using the + operator.

str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print(concatenated_str)

# This will print "Hello World" to the console, demonstrating that the +
# operator is used to concatenate the two strings with a space in between.

# You can also concatenate strings with other data types by converting them to
# strings first using the str() function.

number = 42
concatenated_with_number = str1 + " " + str(number)
print(concatenated_with_number)

# This will print "Hello 42" to the console, demonstrating that the number 42
# is converted to a string and concatenated with "Hello" using the + operator.

# String concatenation can also be done using the join() method, which is more
# efficient for concatenating multiple strings.

str_list = ["Hello", "World", "from", "Python"]
joined_str = " ".join(str_list)
print(joined_str)

# This will print "Hello World from Python" to the console, demonstrating that
# the join() method is used to concatenate the strings in the list with a space
# as the separator.

# You can also use f-strings (formatted string literals) for concatenation,
# which allows you to embed expressions inside string literals.

name = "Aliceex"
greeting = f"Hello, {name}!"
print(greeting)

# This will print "Hello, Alice!" to the console, demonstrating that the
# f-string allows you to embed the variable 'name' directly within the
# string, resulting in a more readable and concise way to concatenate
# strings with variables.

# String concatenation can also be done using the % operator, which is an older
# method for formatting strings.

age = 30
concatenated_with_age = "Hello, I am %d years old." % age
print(concatenated_with_age)

# This will print "Hello, I am 30 years old." to the console, demonstrating
# that the % operator is used to format the string by replacing %d with
# the value of the variable 'age'. However, using f-strings is generally
# recommended over the % operator for string formatting in modern Python
# code due to its improved readability and functionality.

# String concatenation can also be done using the format() method, which is
# another older method for formatting strings.

concatenated_with_format = "Hello, I am {} years old.".format(age)
print(concatenated_with_format)

# This will print "Hello, I am 30 years old." to the console, demonstrating
# that the format() method is used to format the string by replacing {}
# with the value of the variable 'age'. Similar to the % operator,
# using f-strings is generally recommended over the format() method
# for string formatting in modern Python code due to its improved
# readability and functionality.

# Also f-strings is easier for formating multiple variables in a string.

name = "Alex"
age = 30
greeting_with_fstring = f"Hello, my name is {name} and I am {age} years old."
print(greeting_with_fstring)

# This will print "Hello, my name is Alice and I am 30 years old."
# demonstrating that the f-string allows you to embed multiple
# variables directly within the string, resulting in a more readable
# and concise way to concatenate strings with variables compared to
# using the % operator or the format() method.

# string tables
table = "Name\tAge\tCity\nAlex\t30\tThe End\nSteve\t25\tNether"
print(table)
# This will print a formatted table to the console, demonstrating that the \t
# escape character is used to create tab spaces between the columns, and the \n
# escape character is used to create new lines for each row of the table.
