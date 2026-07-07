# Try & Except with Finally

# Finally is used to execute a block of code, no matter what happens in the
# try or except blocks.

def divide(a, b):
    result = 0
    try:
        result = a / b
        print("Result is", result)
        return result
    except ZeroDivisionError as err:
        print("Error:", err)
        return None
    finally:
        print("Finally")


print(divide(1, 2))
print(divide(1, 0))
