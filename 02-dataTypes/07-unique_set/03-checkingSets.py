# Checking Sets

# Checking sets is important because it allows us to determine if an
# element exists within a set or not.
# This can be useful in various scenarios such as validating user input,
# removing duplicates from a list, and more.

# Another example
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Checking if an element is in the set
if 4 in my_set:
    print("4 is in the set")

# #########################################################
# Looking at more complexity
sample_set = {1, 2, 3, 4, 5}

# Now let's check if an element exists within the set using the 'in' keyword
element_to_check = 3
if element_to_check in sample_set:
    print(f"{element_to_check} is in the set.")
else:
    print(f"{element_to_check} is not in the set.")

# We can also use the 'not in' keyword to check if an element does not exist
# within a set
element_to_check = 6
if element_to_check not in sample_set:
    print(f"{element_to_check} is not in the set.")
else:
    print(f"{element_to_check} is in the set.")
    
    

