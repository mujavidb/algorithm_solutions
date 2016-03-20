# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def unique(x):
	length = len(x)
	if length > 255:
		return False
	y = {}
	for z in x:
		if y.has_key(z):
			return False
		else:
			y[z] = 0
	return True

print unique("love!")
print unique("lo0000ve!")