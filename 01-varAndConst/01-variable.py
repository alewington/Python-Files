# Variable is a container for storing data values.
# Its starts lowercase letter and can be a combination of letters and numbers.
# It cannot start with a number.
# It cannot use special symbols or spaces.

x: int = 1
steps_taken: int = 1000
speedOfCar: int = 88
first_name: str = "Yoshi"
random_name: str = "Zhang"
lightsOn: bool = True
list_of_scores: list[int] = [90, 80, 70, 60]

print(x)
print(steps_taken)
print(speedOfCar)
print(first_name)
print(random_name)
print(lightsOn)
print(list_of_scores)

# You can display them in these fashion.
# Chose A style and keep with it!

# e.g. snake_case, camelCase, PascalCase, etc.
snake_case: str = "This is snake_case"  # Typically seen as most used in Python
camelCase: str = "This is camelCase"
PascalCase: str = "This is Pascal Case, don't use"

print(snake_case)  # Typically seen as most used in Python
print(camelCase)
print(PascalCase)  # Don't use PascalCase. too similar to CONSTANTS
print("Choose one style and keep to it!")
