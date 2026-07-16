# OS

# OS module provides a way of using operating system dependent functionality.
import os

# Get the current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# List all files and directories in the current working directory
files_and_dirs = os.listdir(cwd)
print("Files and Directories in '", cwd, "':")
for item in files_and_dirs:
    print(item)

# Create a new directory
new_dir = "test_directory"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print("Directory '", new_dir, "' created.")
else:
    print("Directory '", new_dir, "' already exists.")

# Remove the created directory
if os.path.exists(new_dir):
    os.rmdir(new_dir)
    print("Directory '", new_dir, "' removed.")
