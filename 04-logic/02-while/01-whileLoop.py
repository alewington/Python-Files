# While Loop

# A while loop is used to execute a block of code repeatedly as long as a
# given condition is true. The syntax for a while loop in Python is as
# follows:

#   while <condition>:
#       <block of code>

# Example:
while True:
    user_input: str = input("Enter 'exit' to quit: ")
    if user_input.lower() == 'exit':
        break
    print(f"You entered: {user_input}")
# In the above example, the while loop will continue to execute as long as the
# condition (True) is true. The loop will prompt the user to enter input, and
# if the user enters 'exit', the loop will break and terminate. Otherwise, it
# will print the entered input.
