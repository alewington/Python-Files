# Arrays

# To use arrays properly in Python you need to use the ARRAY module.

# Below information from
# https://www.geeksforgeeks.org/python/difference-between-list-and-array-in-python/

# Arrays

# An array is a data structure that stores elements of the same data type in
# contiguous (next to, near) memory locations, making it efficient for
# numerical operations. Arrays require the array module to be used.

# -Stores of the homogenous (same kind of) data only
# -Uses less memory than lists
# -Faster for numerical and mathematical operations
# -Better suited for large numeric datasets

import array as arr

a: arr.array = arr.array('i', [1, 2, 3])
print(type(a))
for i in a:
    print(i, end=" ")

"""
Basis	                    Array
Data Type Handling	        Stores only one data type
Memory Usage	            Uses less memory because of uniform data type
Performance	                Faster for numeric computations
Flexibility	                Less flexible - fixed type and size constraints
Arithmetic Operations	    Supports element-wise arithmetic
Built-in Support	        Requires importing the array module
Best Use Case	            Numeric and scientific data processing
Data Consistency	        Enforces strict type consistency
"""
