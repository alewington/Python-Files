# File Handling

# File handling is an essential aspect of programming that allows you to read
# from and write to files on your computer. In Python, you can work with files
# using built-in functions and methods.
# The basic operations for file handling include opening a file, reading from
# it, writing to it, and closing it. Python provides a simple and efficient
# way to handle files using the built-in `open()` function.

# The 'import os' is added due to the file path may not always point to where
# you may expect it to be, so we use the os module to get the absolute path
# of the current file and use that file. It is safer and more reliable to use
# the absolute path of the file rather than a relative path.
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'example.txt')

# Example usage of file handling in Python
# Open a file in write mode
with open(file_path, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is an example of file handling in Python.\n")
    file.close()

with open(file_path, "r") as file:
    content = file.read()
    print(content)
    file.close()


# In the above example, we first open a file named "example.txt" in write
# mode, write some text to it, and then close the file. After that, we open
# the same file in read mode, read its content, and print it to the
# console. Finally, we close the file again to free up system resources.
