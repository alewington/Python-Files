# Try & Except Message Chain

# The try and except statements are used to handle exceptions.
# An exception is an error that occurs during the execution of a program.
# When an exception occurs, Python normally stops executing the current code
# and displays an error message.

while True:
    try:
        i: int = int(input('Enter a number: '))
        print(1 / i)
        break
    except (ValueError, TypeError) as e:
        print(f'Error:{e}')
    except ZeroDivisionError:
        print('You can\'t divide by zero')
    print("The program is still running.")
