#Given an input array, remove all any duplicate occurrences and return the array

# only works for strings of alphabetic characters, and prints in alphabetical order
# O(n)
def remove_dups(string):
	new = []
	for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		occur = len([y for y in string if y == x])
		if occur:
			new.append(x)
	print new

# O(n) works for all
def fast_remove(array):
	hashmap = {}
	results = []
	for x in array:
		if not hashmap.has_key(x):
			hashmap[x] = True
			results.append(x)
	print results

def find_dups(array):
	hashmap = {}
	dups = []
	for x in array:
		if hashmap.has_key(x):
			dups.append(x)
		else:
			hashmap[x] = 1
	return dups

def find_dups_best(array):
	"""
	Find all dups in O(n) time and O(1) space
	"""
	dups = []
	for i in range(len(array)):
		if array[abs(array[i])] > 0:
			array[abs(array[i])] = -array[abs(array[i])]
		else:
			dups.append(i)
	return dups


print find_dups_best([1,2,3,2,5,6,4,3])
# remove_dups(["A","R","F","E","R","C","F","X","N","P"])
# fast_remove(["A","R","F","E","R","C","F","X","N","P"])