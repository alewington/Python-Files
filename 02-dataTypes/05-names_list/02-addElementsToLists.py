# Appending Lists

# Appending to a list is adding an element to the end of the list.
# This can be done using the append() method. The append() method takes one
# argument, which is the element you want to add.

# Example:
names: list[str] = ["Alice", "Bob"]
names.append("Charlie")
print(names)  # Output: ['Alice', 'Bob', 'Charlie']

# You can also append another list to a list using the extend() method. The
# extend() method takes one argument, which is the list you want to add.

# Example:
names: list[str] = ["Alice", "Bob"]
more_names: list[str] = ["Charlie", "David"]
names.extend(more_names)
print(names)  # Output: ['Alice', 'Bob', 'Charlie', 'David']

# You can also append an element using the "+" operator. This will create a
# new list with the elements of both lists.

# Example:
names: list[str] = ["Alice", "Bob"]
more_names: list[str] = ["Charlie", "David"]
names = names + more_names
print(names)  # Output: ['Alice', 'Bob', 'Charlie', 'David']

# You can also append an element using the insert() method. The insert()
# method takes two arguments, the index where you want to add the
# element and the element itself.

# Example:
names: list[str] = ["Alice", "Bob"]
names.insert(1, "Charlie")
print(names)  # Output: ['Alice', 'Charlie', 'Bob']

# You can also append an element using the insert() method with a negative
# index. The insert() method will add the element at the end of the list
# if the index is greater than or equal to the length of the list.

# Example:
names: list[str] = ["Alice", "Bob"]
names.insert(-1, "Charlie")
print(names)  # Output: ['Alice', 'Charlie', 'Bob']

# Example:
names: list[str] = ["Alice", "Bob"]
names.insert(-2, "Charlie")
print(names)  # Output: ['Charlie', 'Alice', 'Bob']


# Example:
names: list[str] = ["Alice", "Bob"]
names.insert(0, "Charlie")
print(names)  # Output: ['Charlie', 'Alice', 'Bob']
