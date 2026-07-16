# Maths with float

# this is how to do maths with float numbers
print(.1 + .02 == 0.3000000000000004)
# 0.1 +0.2 == 0.3 # False

print(0.1 + 0.2)
# (0.2 == 0.3)

# why does 0.1 + 0.2 = 0.30000000000000004?
# because of the way computers store numbers

# computer stores a number as binary (base-2)
# so,0.5 is stored as:
print(bin(1))  # 0b1
print(bin(3))  # 0b11
print(bin(7))  # 0b11
print(bin(9))  # 0b1001


# https://0.30000000000000004.com/#:~:text=By%20default%2C%20the%20inputs%200.1,but%20is%20printed%20as%200.3%20.

# Floating Point Math
# Your language isn’t broken, it’s doing floating point math. Computers can
# only natively store integers, so they need some way of representing decimal
# numbers. This representation is not perfectly accurate. This is why, more
# often than not, 0.1 + 0.2 != 0.3.

# Why does this happen?
# It’s actually rather interesting. When you have a base-10 system
# (like ours), it can only express fractions that use a prime factor of the
# base. The prime factors of 10 are 2 and 5. So 1/2, 1/4, 1/5, 1/8, and 1/10
# can all be expressed cleanly because the denominators all use prime factors
# of 10. In contrast, 1/3, 1/6, 1/7 and 1/9 are all repeating decimals because
# their denominators use a prime factor of 3 or 7.

# In binary (or base-2), the only prime factor is 2, so you can only cleanly
# express fractions whose denominator has only 2 as a prime factor. In binary,
# 1/2, 1/4, 1/8 would all be expressed cleanly as decimals, while 1/5 or 1/10
# would be repeating decimals. So 0.1 and 0.2 (1/10 and 1/5), while clean
# decimals in a base-10 system, are repeating decimals in the base-2 system
# the computer uses. When you perform math on these repeating decimals, you
# end up with leftovers which carry over when you convert the computer’s
# base-2 (binary) number into a more human-readable base-10 representation.

# Below are some examples of sending .1 + .2 to standard output in a variety
# of languages.
