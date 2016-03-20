def shift(array, shift): 
	return array[shift:] + array[:shift]

print shift("lovefun", 4)