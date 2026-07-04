# Nesting

# The following code is a bit of a mess, but it works!

# Let's clean it up by using some indentation to make it more readable.
if True:
    if True:
        print("This is nested inside the first if statement.")
    else:
        print("This is the else block of the first if statement.")

print("This is outside all of the if statements.")

# The following code will not run because it is indented too far.
if True:
    if True:
        print("This is nested inside the first if statement.")
    else:
        print("This is the else block of the first if statement.")

    print("This is outside all of the if statements.")

# nesting 3 layers deep
if True:
    if True:
        if True:
            print("This is nested inside the second if statement.")
        else:
            print("This is the else block of the second if statement.")
    else:
        print("This is the else block of the first if statement.")
else:
    print("This is the else block of the outermost if statement.")

#############################################################################
# These programs show that you can have as many layers of nesting as you want,
# but it can get confusing quickly. It's usually a good idea to keep your
# code as flat as possible to make it easier to read and understand.
# Sometimes there are better ways to structure your code to avoid deep
# nesting, such as using functions or breaking the logic into smaller pieces.
# We will go on to functions later in the course, but for now, let's just
# focus on understanding how nesting works and how to use it effectively.
##############################################################################
