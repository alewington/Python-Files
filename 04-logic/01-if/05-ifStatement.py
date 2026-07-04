# You can also use multiple if statements to check for more conditions.
# Syntax:
#   if <condition>:
#       <block of code>
#   if <condition>:
#       <block of code>
#   else:
#       <block of code>

# Example:
x: int = 5
if x > 0:
    print("x is positive")
if x < 0:
    print("x is negative")
else:
    print("x is zero")

# The above example will print "x is positive" because the condition (x > 0)
# is true.
# If x was -5, it would print "x is negative".
# If x was 0, it would print "x is zero".

# The benefit of this method is it is easier to read and understand,
# especially when there are many conditions to check. However,
# it can also lead to more code being executed than necessary,
# as all conditions will be checked even if one is true.
