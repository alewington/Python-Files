# Mixed Datatypes in Lists

# You can have mixed datatypes in Lists by
# adding more than one data type to the list.

# For example, you could add more than one string or number to the list.

# This is an example of a list with strings and numbers:

mixed_list: list[int | str] = [1, "hello", 2]
print(mixed_list)

# This is an example of a list with strings and lists:

mixed_list2: list[str | list[str]] = ["hello", ["hi", "hey"], "goodbye"]
print(mixed_list2)

# You can also add more than one data type to the dictionary.

# For example, you could add more than one string or number to the dictionary.

# This is an example of a dictionary with strings and numbers:

dictionary: dict[int, str] = {1: "hello", 2: "goodbye"}
print(dictionary)

# This is an example of a dictionary with strings and lists:

dictionary2: dict[str, list[str] | str] = {
    "hi": ["hello", "hey"],
    "goodbye": "goodbye"
    }
print(dictionary2)
