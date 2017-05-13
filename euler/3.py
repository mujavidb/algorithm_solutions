# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def is_prime(n):
	for i in range(2,int(n ** 0.5)):
		if n % i == 0:
			return False
	return True

highest = 0
start = 600851475143

for i in range(1, start, 2):
	if i > 100000:
		break
	if start % i == 0 and is_prime(i):
		highest = i

print(highest)

