# Using Comparison Operators

# You can use comparison operators in loops, if statements, while loops
# and other areas requiring a boolean based test

# IF example:
print("-"*50)
print("IF Statement example")
print("-"*50)
weather = "hot"

if weather == "hot":
    print("I'm going to the beach!")
else:
    print("I'm staying home.")

# Which option will it print and why?
# How can you be certain it will only print one of them?

# Run the code to find out.

# For Loop example
print("-"*50)
print("For Loop example")
print("-"*50)
times_table = 10
for i in range(1, times_table + 1):
    if i == 5:
        break
    print("{} x {} = {}".format(i, times_table, i * times_table))

# Which option will it print and why? Maybe when?

# Run the code to find out.

# While Loop example
print("-"*50)
print("While Loop example")
print("-"*50)
times_table = 10
i = 1
while i < times_table:
    if i == 5:
        break
    print("{} x {} = {}".format(i, times_table, i * times_table))
    i += 1
# Which option will it print and why? Maybe when?
# what is different between the For and While Loop versions?

# Is there advantages and disadvantages?
