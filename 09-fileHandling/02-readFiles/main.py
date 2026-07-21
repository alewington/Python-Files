# Reading files
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'example.txt')

# You can use the 'with' statement to automatically close the file
with open(file_path, 'r') as file:
    content = file.read()
    print(content)

# This code reads the entire content of the file at once and prints it to the
# console. The 'with' statement is used to open the file, which ensures that
# the file is properly closed after its suite finishes, even if an exception
# is raised.


# You can also read the file line by line
with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())
# Use strip() to remove any leading/trailing whitespace

# This code allows you to read the contents of a file in Python. The 'with'
# statement is used to open the file, which ensures that the file is properly
# closed after its suite finishes, even if an exception is raised. The first
# block reads the entire content of the file at once, while the second block
# reads the file line by line, which can be more memory efficient for large
# files. The strip() method is used to remove any leading or trailing
# whitespace from each line before printing it.
