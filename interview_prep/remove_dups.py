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

remove_dups(["A","R","F","E","R","C","F","X","N","P"])
fast_remove(["A","R","F","E","R","C","F","X","N","P"])