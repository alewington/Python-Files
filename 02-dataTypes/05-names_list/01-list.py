# Lists

# Lists are ordered collections of items. Items can be of different types.
# For example, a list could contain strings, integers, and even other lists.
# it may look similar to arrays and can be used similarly to arrays
# but Lists are not arrays.

# More info about Lists vs. Arrays can be found here:
# https://www.geeksforgeeks.org/python/difference-between-list-and-array-in-python/
# I will cover arrays later in the lessons.

names: list[str] = ["Steve", "Alex"]
print(names)

# 1. Accessing List Elements
print(names[0])

# 2. Modifying List Elements
names.append("Ender Dragon")
print(names)

# 3. Pop the last name from the list
names.pop()
print(names)

# 4. Sort list descending alphabetically
names.sort(reverse=True)
print(names)

'''
Basis	                List
Data Type Handling	    Can store mixed data types
Memory Usage	        Uses more memory due to flexible storage
Performance	            Slower for numerical operations
Flexibility	            Supports easy insertion, deletion and resizing
Arithmetic Operations	Cannot perform element-wise arithmetic directly
Built-in Support	    Available by default in Python
Best Use Case	        General-purpose and mixed-type data
Data Consistency	    Allows mixed values without restriction

Compared to array module.
'''
