from sympy import primerange

# Generate the first few primes and pick an 8-digit prime
primes = list(primerange(10000000, 100000000))
eight_digit_prime = primes[0]

eight_digit_prime

print(eight_digit_prime)