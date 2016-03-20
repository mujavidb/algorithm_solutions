from math import sqrt, floor

def isPrime(x):
	if isPrime == 1:
		return False
	checks = [ a for a in range(2, int(floor(sqrt(x))), 2)]
	for b in range(len(checks)):
		if x % checks[b] == 0: return False
	return True

print isPrime(12)
print isPrime(11)
print isPrime(3571)