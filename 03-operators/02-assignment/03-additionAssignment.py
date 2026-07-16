# Addition Assignment

# Using addition assignment
x: int = 1
y: int = 2
z: int = x + y
print(z)  # 3

# Using the += operator
x: int = 1
y: int = 2
x += y
print(x)  # 3

# incrementing with +=
x: int = 0
for i in range(5):
    x += 1
    print(i, ". Add 1 = ", x)  # Output: 1-5
