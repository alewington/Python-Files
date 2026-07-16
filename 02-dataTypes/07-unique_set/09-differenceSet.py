# Set difference

# The difference() method returns a set that contains the difference between
# two sets.
# In other words, it returns a set that contains the elements that are present
# in the first
# set but not in the second set. You can also use the `-` operator to achieve
# the same result.
set1: set[int] = {1, 2, 3, 4}
set2: set[int] = {3, 4, 5, 6}
print(f"{set1=}")
print(f"{set2=}")

# Using the difference() method
differenceSet: set[int] = set1.difference(set2)
print(f"Difference using difference() method: {differenceSet}")

# Using the - operator
differenceSetOperator: set[int] = set1 - set2
print(f"Difference using - operator: {differenceSetOperator}")

# Both methods will give you the same result, which is a new set
# containing the elements that are present in `set1` but not in `set2`.
# In this case, the difference will be `{1, 2}`.

# Note that the order of the sets matters when calculating the difference.

# Now to demonstrate the difference in the other direction:
# Using the difference() method
differenceSetReverse: set[int] = set2.difference(set1)
print(f"""
      Difference in reverse using difference() method:{differenceSetReverse}
      """)

# Using the - operator
differenceSetReverseOperator: set[int] = set2 - set1
print(f"""
      Difference in reverse using - operator:{differenceSetReverseOperator}
      """)
