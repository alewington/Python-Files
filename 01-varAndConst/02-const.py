# Constants

# Constants are values that cannot be changed.
# In Python, we can use the 'const' keyword to declare a constant value.
# However, Python does not have a built-in 'const' keyword.
# Instead, we can use a convention to indicate that a vae is a constant
# by using uppercase

PI = 3.14
GRAVITY = 9.8
SPEED_OF_LIGHT = 299792458

# In the above code, we have declared three constants: PI, GRAVITY, and
# SPEED_OF_LIGHT.
# By convention, we use uppercase letters to indicate that these variables are
# constants.
# Although we can change the value of these variables, it is not recommended
# as it goes against the convention and can lead to confusion for other
# developers who may read our code.

# ---------------------------------------------------------------------------
# ADVANCED
# In Python, we can also use the 'final' keyword from the 'typing' module to
# indicate that a variable is a constant.

from typing import final  # This should be at the top of the page!
# breaking flake e402.


@final
class Constants:
    PI = 3.14
    GRAVITY = 9.8
    SPEED_OF_LIGHT = 299792458

# In the above code, we have defined a class called 'Constants' and decorated
# it with the '@final' decorator. We can access the constants defined in the
# 'Constants' class using the class name, like this:


print(Constants.PI)
print(Constants.GRAVITY)
print(Constants.SPEED_OF_LIGHT)


# Output:
# 3.14
# 9.8
# 299792458
