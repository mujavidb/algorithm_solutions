# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def is_prime(n):
	sqrt = int(n ** 0.5)
	if n in (0,1):
		return False
	for i in range(2,sqrt+1):
		if n % i == 0:
			return False
	return True

total = 0
for i in range(2000001):
	if is_prime(i):
		total += i

print(total)