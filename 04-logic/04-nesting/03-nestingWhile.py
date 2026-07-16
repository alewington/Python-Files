# Nesting While Loops

# The following code demonstrates how to nest while loops.

# In this example, the outer loop will run until i is equal to 10.
i: int = 1
while i <= 10:
    # The inner loop will run until j is equal to 5.
    j = 1
    while j <= 5:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1
# Expected Output
# i: 1, j: 1
# i: 1, j: 2
# i: 1, j: 3
# i: 1, j: 4
# i: 1, j: 5
# i: 2, j: 1
# i: 2, j: 2
# i: 2, j: 3
# i: 2, j: 4
# i: 2, j: 5
# i: 3, j: 1
# i: 3, j: 2
# i: 3, j: 3
# i: 3, j: 4
# i: 3, j: 5
# i: 4, j: 1
# i: 4, j: 2
# i: 4, j: 3
# i: 4, j: 4
# i: 4, j: 5
# i: 5, j: 1
# i: 5, j: 2
# i: 5, j: 3
# i: 5, j: 4
# i: 5, j: 5
# i: 6, j: 1
# i: 6, j: 2
# i: 6, j: 3
# i: 6, j: 4
# i: 6, j: 5
# i: 7, j: 1
# i: 7, j: 2
# i: 7, j: 3
# i: 7, j: 4
# i: 7, j: 5
# i: 8, j: 1
# i: 8, j: 2
# i: 8, j: 3
# i: 8, j: 4
# i: 8, j: 5
# i: 9, j: 1
# i: 9, j: 2
# i: 9, j: 3
# i: 9, j: 4
# i: 9, j: 5
# i: 10, j: 1
# i: 10, j: 2
# i: 10, j: 3
# i: 10, j: 4
# i: 10, j: 5

# In this example, we can see that the outer loop runs 10 times, and for each
# iteration of the outer loop, the inner loop runs 5 times. This results in a
# total of 50 iterations (10 * 5) and prints all combinations of i and j from
# 1 to 10 and 1 to 5, respectively.
