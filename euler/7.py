# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(n):
	sqrt = int(n ** 0.5)
	for i in range(2,sqrt+1):
		if n % i == 0:
			return False
	return True

count = 1
val_prime = 0
current = 2

while count < 10002:
	if is_prime(current):
		count += 1
		if count == 10002:
			val_prime = current
			break
	current +=1

print(val_prime)