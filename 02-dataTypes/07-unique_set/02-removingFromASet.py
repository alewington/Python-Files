# Removing from a set

# Removing from a set using the remove() method.
# All you have to do is call the remove() method
# on your set and pass in the value that you want to remove.

my_set: set[int] = {1, 2, 3, 4, 5}
print(my_set)

# Removing an element from a set
my_set.remove(3)
print(my_set)
