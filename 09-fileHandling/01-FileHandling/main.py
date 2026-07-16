# Open vs With Open

import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'example.txt')


# Open a file using the open() function
file = open(file_path, "r")
content = file.read()
print(content)
file.close()  # Don't forget to close the file

# vs.

# Open a file using the 'with' statement
with open(file_path, "r") as file:
    content = file.read()
    print(content)

# The 'with' statement automatically closes the file after the block of code is
# executed, even if an error occurs. This is a better practice than manually
# opening and closing files.

# Other benefits to with statement include better readability and less chance
# of forgetting to close the file, which can lead to resource leaks.
# plus auto saving and handling exceptions.

# easier to read and understand, especially for larger code blocks that involve
# multiple file operations. It clearly indicates that the file is being used
# within a specific context and will be automatically closed when the block is
# exited. This can help prevent errors and make the code more maintainable.
