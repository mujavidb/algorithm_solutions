# Given an array, find out if the sum of any two
# numbers from the array is equal to zero and return the two numbers

# O(n^2)
def zerosum_slow(array):
	results = []
	for x in range(len(array)):
		for y in array[x + 1:]:
			if array[x] + y == 0:
				results.append([array[x], y])
	print results 

# O(n)
def zerosum(array):
	results = []
	hashmap = {}
	for x in array:
		if hashmap.has_key(x):
			results.append([x, hashmap[x]])
		else:
			key = -1 * x
			hashmap[key] = x
	print results


zerosum_slow([4,5,0,-5,0,8 ,-6, 12])
zerosum([4,5,0,-5,0,8 ,-6, 12])