# deleting files

# This script demonstrates how to delete files in Python using the built-in
# `os` module. It checks if the file exists before attempting to delete it.
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'example.txt')

# check if the file exists before attempting to delete it
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")
elif not os.path.exists(file_path):
    with open(file_path, 'w') as file:  # this is the point the file is created
        file.write("Hello, World!\n")
        file.write("This is a new file created using Python.\n")
    print(f"File '{file_path}' did not exist, so it was created.")
else:
    print(f"Unknown Status for file '{file_path}'.")

# Note: Be cautious when deleting files, as this action is irreversible.
# Always ensure that you are deleting the correct file and that you have
# backups if necessary.

# You can also use the `os.unlink()` method to delete a file, which is
# functionally equivalent to `os.remove()`. Both methods will remove the
# specified file from the filesystem.


# You may want to add checks like:
# "Are you sure you want to delete this file? (y/n)"
# before deleting a file to prevent accidental deletions.
