# Nesting For Loops

for i in range(1, 6):
    for j in range(1, 6):
        print(f"i: {i}, j: {j}")

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

# from this example, we can see that the outer loop runs 5 times, and for each
# iteration of the outer loop, the inner loop also runs 5 times. This results
# in a total of 25 iterations (5 * 5) and prints all combinations of
# i and j from 1 to 5.
