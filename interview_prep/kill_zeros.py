# Remove all zeros of an array to the right
# O(n)

def kill_zeros(array):
	i = 0
	while i < len(array):
		if array[i] == 0:
			del array[i]
		else:
			i+=1
	print array

kill_zeros([4,5,6,7,0,0,3,4,0,3,6,0,0,8])