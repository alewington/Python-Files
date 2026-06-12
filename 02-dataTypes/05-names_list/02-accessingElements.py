# Accesing Elements

# 01 - Accessing the First Element
names = ["Alice", "Bob", "Charlie"]
print("First name:", names[0])

# 02 - Accessing the Last Element
last_name = names[-1]
print("Last name:", last_name)

# 03 - Accessing an Element at a Specific Index
specific_index = 2
element_at_index = names[specific_index]
print(f"Element at index {specific_index}:", element_at_index)

# Simplified
names = ["Steve", "Alex"]
print(names)


print(names[0])

# accesing a range of elements
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# 03 - Accessing Elements from Index 1 to 3 (inclusive)
range_of_names = names[1:4]
print("Range of names:", range_of_names)

# 04 - Accessing Elements from the Second Last to the End
last_range_of_names = names[-2:]
print("Last range of names:", last_range_of_names)
