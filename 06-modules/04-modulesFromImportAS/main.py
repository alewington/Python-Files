# Use As on from import

# Adding as allows you to use the module in a different way than importing it.
# This is useful when you want to import multiple modules that have the same
# name, but are from different packages.
# The benefit of as here is that you don't need to type the full path to the
# function, but instead just the name of the function.
# e.g. math.sqrt(x) becomes sqrt(x). or square_root with as.

from math import sqrt as square_root
print(square_root(25))

# You can also use as to rename a modules function
