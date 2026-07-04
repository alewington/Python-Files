# Example:
while True:
    user_input: str = input("Enter a number (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    try:
        number: int = int(user_input)
        if number < 0:
            print("Please enter a positive number.")
            continue
        print(f"You entered the positive number: {number}")
    except ValueError:
        print("That's not a valid number. Please try again.")
# In this example, the while loop will continue to prompt the user for input
# until they enter 'exit'. If the user enters a valid number, it will check if
# the number is positive. If the number is negative, it will prompt the user
# to enter a positive number and continue the loop. If the input is not a valid
# number, it will catch the ValueError and prompt the user to try again.
