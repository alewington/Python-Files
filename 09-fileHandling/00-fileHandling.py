# File Handling

# File handling is an essential aspect of programming that allows you to read
# from and write to files on your computer. In Python, you can work with files
# using built-in functions and methods.
# The basic operations for file handling include opening a file, reading from
# it, writing to it, and closing it. Python provides a simple and efficient
# way to handle files using the built-in `open()` function.

# Example usage of file handling in Python
# Open a file in write mode
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This is an example of file handling in Python.\n")
file.close()

# Open the file in read mode
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# In the above example, we first open a file named "example.txt" in write
# mode, write some text to it, and then close the file. After that, we open
# the same file in read mode, read its content, and print it to the
# console. Finally, we close the file again to free up system resources.
