# Writing to Files

# In Python, you can write to files using the built-in `open()` function along
# with the `write()` method. Here's a simple example of how to write to a
# text file:

import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'example.txt')

# check if the file exists before writing to it
if os.path.exists(file_path):
    with open(file_path, 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a new file created using Python.\n")
    print(f"File '{file_path}' written successfully.")
else:
    print(f"File '{file_path}' does not exist. Please create the file first.")

# You can also write multiple lines to a file at once using the `writelines()`
# method. Here's an example:
lines = [
    "Line 1: This is the first line.\n",
    "Line 2: This is the second line.\n",
    "Line 3: This is the third line.\n"
]
with open(file_path, 'w') as file:
    file.writelines(lines)
# This code writes multiple lines to the file 'example.txt' at once. The
# `writelines()` method takes a list of strings and writes them to the file.
