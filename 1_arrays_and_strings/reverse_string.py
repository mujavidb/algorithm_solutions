def reversi(x):
	y = ""
	for sub in x: y = sub + y
	return y

def reverso(x):
	y = ""
	for z in range(len(x)): y += x[-1 * (z + 1)]
	return y

#Above solution as a list comprehension joined into a string
def reversa(x):
	return "".join([ x[ -1 * (y + 1)] for y in range(len(x)) ])

def reverse(x):
	if not x: return []
	return reverse(x[1:]) + [x[0]]

def reversu(x):
	return x[::-1]

print reversi("Love and Peace!")
print reverso("Love and Peace!")
print reversa("Love and Peace!")