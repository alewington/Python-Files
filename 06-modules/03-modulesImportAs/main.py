# Use as on Import

# Using as on importing a module allows you to use the module's name as an
# alias for the imported object.
# The benefit is 2 fold:
# - You can import multiple modules with the same name, and avoid conflicts.
# - You can import a module under a different name.

import math as m  # Importing math as m

# think of it a renaming a module for the program.

print(m.sqrt(16))  # Using m instead of math
