# Mixed Nesting

# The following code demonstrates how to mix different types of nesting, such
# as if statements, for loops, and while loops.

# Example program with a mixture of if, for, and while loops
for i in range(1, 4):
    print(f"Outer loop iteration: {i}")

    if i % 2 == 0:
        print("This is an even iteration.")
    else:
        print("This is an odd iteration.")

    j = 1
    while j <= 3:
        print(f"  Inner while loop iteration: {j}")

        for k in range(1, 4):
            print(f"    Innermost for loop iteration: {k}")

        j += 1

# Expected Output
# Outer loop iteration: 1
# This is an odd iteration.
#   Inner while loop iteration: 1
#     Innermost for loop iteration: 1
#     Innermost for loop iteration: 2
#     Innermost for loop iteration: 3
#   Inner while loop iteration: 2
#     Innermost for loop iteration: 1
#     Innermost for loop iteration: 2
#     Innermost for loop iteration: 3
#   Inner while loop iteration: 3
#     Innermost for loop iteration: 1
#     Innermost for loop iteration: 2
#     Innermost for loop iteration: 3
# Outer loop iteration: 2
# This is an even iteration.
#   Inner while loop iteration: 1
#     Innermost for loop iteration: 1
#     Innermost for loop iteration: 2
#     Innermost for loop iteration: 3
#   Inner while loop iteration: 2
#     Innermost for loop iteration: 1
#     Innermost for loop iteration: 2
#     Innermost for loop iteration: 3
#   Inner while loop iteration: 3
#     Innermost for loop iteration: 1
#     Innermost for loop iteration: 2
#     Innermost for loop iteration: 3
# Outer loop iteration: 3
# This is an odd iteration.
#   Inner while loop iteration: 1
#     Innermost for loop iteration: 1
#     Innermost for loop iteration: 2
#     Innermost for loop iteration: 3
#   Inner while loop iteration: 2
#     Innermost for loop iteration: 1
#     Innermost for loop iteration: 2
#     Innermost for loop iteration: 3
#   Inner while loop iteration: 3
#     Innermost for loop iteration: 1
#     Innermost for loop iteration: 2
#     Innermost for loop iteration: 3

########################################################################
# Example program with a mixture of if, for, and while loops.
# This just demonstrates how the logic / flowcontrol go together.
# Functions are not covered in this chapter, but are important to know about.
# They allow you to group code into reusable blocks that can be called from
# anywhere else in your program. This helps you avoid repeating yourself and
# makes it easier to read and understand your code.
########################################################################
