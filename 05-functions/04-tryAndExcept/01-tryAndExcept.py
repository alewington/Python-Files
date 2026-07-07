# Try & Except

# Try & except allows you to catch an error and do something about it.
# This is useful when you want to run a program, but if there's an error,
# you can handle the error without stopping your code from running.

# Here's an example of a try & except block:
try:
    print(1 / 0)
except ZeroDivisionError:
    print("You tried to divide by zero!")

print("The program is still running.")
