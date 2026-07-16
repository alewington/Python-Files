# For Loop

# Create a list of the first 30 Fibonacci numbers.
fibonacci: list[int] = [0, 1]
for i in range(2, 30):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
print(fibonacci)
