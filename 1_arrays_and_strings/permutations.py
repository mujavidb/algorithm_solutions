def permutations(string1, string2):
	short = string2 if len(string1) > len(string2) else string1
	short_length = len(short)
	long = string1 if len(string1) > len(string2) else string2
	index = long.index(short[0])
	if index == -1:
		return False
	for x in range(index, len(long) - 1):
		if x - index > short_length:
			return True
		if short[x - index] == long[x]:
			continue
		else:
			return False

print permutations("key", "donkey")
print permutations("key", "donkyy")