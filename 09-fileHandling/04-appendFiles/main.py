# Appending to Files

# In Python, you can append to files using the built-in `open()` function along
# with the `a` mode. Here's a simple example of how to append to a text file:

import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'example.txt')

# check if the file exists before appending to it
if os.path.exists(file_path):
    with open(file_path, 'a') as file:
        file.write("Appending a new line to the file.\n")
    print(f"File '{file_path}' appended successfully.")
else:
    print(f"File '{file_path}' does not exist. Please create the file first.")

# You can also append multiple lines to a file at once using the `writelines()`
# method. Here's an example:
lines = [
    "Line 4: This is the fourth line.\n",
    "Line 5: This is the fifth line.\n",
    "Line 6: This is the sixth line.\n"
]
with open(file_path, 'a') as file:
    file.writelines(lines)
# This code appends multiple lines to the file 'example.txt' at once. The
# `writelines()` method takes a list of strings and appends them to the file.
# Note that you need to include newline characters ('\n') at the end of each
# line to ensure that each line is written on a new line in the file.
