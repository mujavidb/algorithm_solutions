# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from functools import reduce

def lcm(x, y):
	big = max(x,y)
	while(True):
		if big % x == 0 and big % y == 0:
			lcm = big
			break
		big += 1
	return lcm


print(reduce(lcm, (x for x in range(1,21))))
