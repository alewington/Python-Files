# You can also use multiple elif statements to check for more conditions.

# Syntax:
#   if <condition>:
#       <block of code>
#   elif <condition>:
#       <block of code>
#   elif <condition>:
#       <block of code>
#   else:
#       <block of code>

# Example:
x: int = 5
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is not a real number")

# The above example will print "x is positive" because the condition (x > 0)
# is true.
# If x was -5, it would print "x is negative".
# If x was 0, it would print "x is zero".
