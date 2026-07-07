# Unexpected errors

# How to handle unexpeted errors?
# 1. Use the try and except statement
# 2. Use the finally statement

try:
    result: int = int('ten')
except Exception as err:  # end alternate constructor
    print(f'Error: "{err} ({type(err)})"')

print()
