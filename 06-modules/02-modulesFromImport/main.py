# Modules

# from module import function
from math import sqrt

print(sqrt(14))

# from module import *
# Try to avoid star * as it imports everything in the module and when you use
# multiple modules, there is a chance of name collision. When this happens the
# last one imported will replace the previous one and be used.
