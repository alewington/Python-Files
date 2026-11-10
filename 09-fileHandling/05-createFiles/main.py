# Create files

# This script demonstrates how to create files in Python using the built-in
# `open()` function.
# Define the file path
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'example.txt')

# check if the file exists before creating it
if not os.path.exists(file_path):
    # Create a new file and write some content to it
    with open(file_path, 'w') as file:  # this is the point the file is created
        file.write("Hello, World!\n")
        file.write("This is a new file created using Python.\n")
    print(f"File '{file_path}' created successfully.")
else:
    print(f"File '{file_path}' already exists. you may delete it")


# You can also create a file and write multiple lines at once using the
# `writelines()` method.
lines = [
    "Line 1: This is the first line.\n",
    "Line 2: This is the second line.\n",
    "Line 3: This is the third line.\n"
]
with open(file_path, 'w') as file:
    file.writelines(lines)
# This code creates a new file named 'example.txt' and writes multiple lines
# to it at once. The `writelines()` method takes a list of strings and
# writes them to the file. Note that you need to include newline characters
# ('\n') at the end of each line to ensure that each line is written on
# a new line in the file.
