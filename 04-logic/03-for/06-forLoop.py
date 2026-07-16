# For Loop

# Create a list of the first 100 prime numbers.
primes: list[int] = [2]
for n in range(3, 1000, 2):
    is_prime = True
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
        if len(primes) == 100:
            break
print(primes)
