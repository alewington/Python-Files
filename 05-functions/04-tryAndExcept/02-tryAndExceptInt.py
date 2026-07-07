# Try & Except

print("Enter two numbers.")
while True:
    try:
        num_one = int(input("First number: "))
        num_two = int(input("Second number: "))
        print(f'The sum is {num_one + num_two}.')
        break
    except ValueError:
        print('Please enter a valid integer.')

# This program will continually loop until the user enters two integers.
# If the user does not enter an integer, it will keep asking them to do so.
# Once they have entered two integers, it will display their sum.
