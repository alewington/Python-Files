
# Unpacking a List

# Unpacking a list to variables 1 at a time  using for
name_list: list[str] = ["Steve", "Alex", "Creeper"]

print(name_list[0])
print(name_list[1])
print(name_list[2])

# packing a to variable
first_name: str
second_name: str
third_name: str
first_name, second_name, third_name = name_list
print(first_name)
print(second_name)
print(third_name)

# You can also use a longer method
# this will allow you to assign individually, and you won't get errors is
# anything is missed like out of range i.e to many or to few.

name_one: str = name_list[0]
name_two: str = name_list[1]
name_three: str = name_list[2]

print(name_one)
print(name_two)
print(name_three)

# sometimes long lists are just best kept in a list
# you can then use loops to output like so

for i in enumerate(name_list):
    print(i)
