# Casting

# A datatype is the structure of the data.
# Python has several built-in datatypes,
# such as int, float, str, list, tuple, dict, etc.
# Python can recognise the datatype of the variable
# based on the values structure.

speed_of_car: int = 88
# int due to whole number
grams_of_flour: float = 100.5
# float due to decimal number
first_name: str = "Steve"
# str , string due to speech marks
is_raining: bool = False
# bool , boolean due to use of True or False
list_of_fruits: list[str] = ["apple", "Golden Apple", "Enchanted Golden Apple"]
# list due to use of square brackets
person_info: dict[str, str | int] = {"name": "Alex", "age": 30}
# dict , dictionary due to use of curly brackets and key-value pairs.

# In Python, we can convert one datatype to another using casting.
# We can force and change the datatype through "casting" or "type conversion".
# The built-in functions for casting are:
# int() - converts to integer
# float() - converts to float
# str() - converts to string

# Example of casting
number_of_cars: int = 5
print(type(number_of_cars))  # Output: <class 'int'>
number_of_cars_str: str = str(number_of_cars)
print(number_of_cars_str)  # Output: '5'
print(type(number_of_cars_str))  # Output: <class 'str'>
# In this example, we have an integer variable number_of_cars, and we convert
# it to a string using the str() function. The resulting variable
# number_of_cars_str is now a string representation of the original
# integer value.

# other examples of casting
pi: float = 3.14159
pi_int: int = int(pi)
print(pi_int)  # Output: 3
print(type(pi_int))  # Output: <class 'int'>

age_str: str = "25"
age_int: int = int(age_str)
print(age_int)  # Output: 25
print(type(age_int))  # Output: <class 'int'>

is_raining: bool = bool(False)
print(is_raining)  # Output: 'False'
print(type(is_raining))  # Output: <class 'bool'>
