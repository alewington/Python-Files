# String Formatting

# strings are immutable in Python.
# Immutable means that once a string is created, it cannot be changed.
# Any operation that seems to modify the string actually creates a new one.
# So we are creating the string, destroying the string and creating a new one.

# We can format strings in differents ways.
# Using % operator
name: str = "Ghast"
age: int = 150
print("%s is %d years old" % (name, age))  # Using % method

print("{} is {} years old".format(name, age))  # Using .format() method

print(f"{name} is {age} years old")  # Using f-string method
print(f"{name} is {age} years old")

# You can use the % operator to insert variables into a string:
# Using %s for (strings)
print("Hello, %s!" % name)  # Output: Hello, Ghast!
# Using %d for (integers)
print("I have %d apples." % 5)  # Output: I have 5 apples.


# You can use the format() method to insert variables into a string:
print("Hello, {}!".format(name))  # Output: Hello, Ghast!
print("I have {0} apples.".format(5))  # Output: I have 5 apples

# other formatting for strings
# Name,Age,City,
# Alice,30,New York
# Bob,25,Los Angeles

# string f-string tables with formatting

name1: str = "Steve"
age1: int = 30
city1: str = "Nether"
name2: str = "Alex"
age2: int = 25
city2: str = "The End"
table_with_fstring: str = (
    f"{'-'*63}\n"
    f"{'Name':^20}|{'Age':^20}|{'City':^20}|\n"
    f"{'-'*63}\n"
    f"{name1:^20}|{age1:^20}|{city1:^20}|\n"
    f"{name2:^20}|{age2:^20}|{city2:^20}|\n"
    )
print(table_with_fstring)

# This will print a formatted table to the console, demonstrating that the
# f-string allows you to embed variables directly within the string,
# and the \n escape character is used to create
# new lines for each row of the table. The resulting output will be:
# ---------------------------------------------------------------
#        Name         |        Age          |        City         |
# ----------------------------------------------------------------
#       Alice         |        30           |     New York        |
#       Bob           |        25           |   Los Angeles       |

# The full correct method will be shown with loops later.

# Playing with the gaps

print(f"{name1:,^30}")
print(f"{name1:^30}")
print(f"{name1:,<30}")  # default
print(f"{name1:<30}")  # default
print(f"{name1:,>30}")
print(f"{name1:>30}")

# putting in calculations to f-string

print(f" {5*3:->10} Meters")
print(f"£{15.00+13.75:->10}")
