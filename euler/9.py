# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


for i in range(1000):
	for j in range(i,1000):
		square_sum = (i**2) + (j**2)
		root_square = (square_sum ** 0.5)
		total = i + j + root_square
		if total > 1000:
			break
		if root_square > j and total == 1000:
			print(i * j * root_square)

