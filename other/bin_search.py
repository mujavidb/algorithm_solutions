#move left pointer to position of v

def binSearch(array, v):
	left = 0
	right = len(array)
	while left < right:
		center = int((left + right)/2)
		if v > array[center]:
			left = center + 1
		else:
			right = center
	return left

a = [1,2,4,5,7,10,13,15]
v = 10
print binSearch(a,v)