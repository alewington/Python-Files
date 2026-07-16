# Removing elements from a Tuple

# You can remove elements from a tuple by
# assigning the tuple to a new variable and then using a slice notation to
# exclude the element(s) you want removed.

# Note: this is a destructive operation, in that it modifies the original
# tuple.
# Should tuples really be modified?
# It's generally considered better to create new tuples rather than modify
# existing ones.
# See also:
# https://stackoverflow.com/questions/1537202/remove-element-from-a-tuple
# Let's create the tuple we want to remove an element from.
# The tuple is created using a list of values in parentheses, with commas
# separating each value.
# Note: tuples are immutable, so you can't change them after they have been
# created.

# In this example, the tuple will be named "myTuple" and it will contain 3
# elements: 0, 1, and 2.

myTuple: tuple[int, ...] = (0, 1, 2)
print(myTuple)

# Now let's remove the first element from the tuple.

# To do this, we can use a slice notation to exclude the first element of the
# tuple.
# Here is an example:

myTuple: tuple[int, ...] = myTuple[1:]
print(myTuple)

# The result of this will be (1, 2).
# Note that the first element has been removed.

# Now let's remove more than one element from a tuple.

# To do this, we can use a slice notation to exclude multiple elements of the
# tuple.
# Here is an example:

myTuple: tuple[int, ...] = myTuple[2:]
print(myTuple)

# The result of this will be (2).
# Note that both the first and second element have been removed.

# Now let's remove all elements from a tuple.

# To do this, we can use an empty slice notation to exclude all elements of
# tuple.
# Here is an example:

myTuple: tuple[int, ...] = myTuple[:0]
print(myTuple)

# The result of this will be ().
# Note that all elements have been removed.

# Now let's remove a specific element from a tuple.

# To do this, we can use slice notation to exclude the element you want to
# remove.
# Here is an example:

myTuple: tuple[int, ...] = myTuple[:1] + (3,) + myTuple[2:]
# This is a tuple with 4 elements:
# 0, 3, 1, and 2.
print(myTuple)

# The result of this will be (0, 3, 1, 2).
# Note that the second element has been replaced by the number 3.

# The example below removes the first element (0) of the tuple.
t: tuple[int, ...] = (1, 2, 3, 4, 5)
print(t)  # Prints (1, 2, 3, 4, 5)
t = t[1:]  # Remove first element by assigning a slice of the tuple from the
# second element to the end.
print(t)  # Prints (2, 3, 4, 5)
