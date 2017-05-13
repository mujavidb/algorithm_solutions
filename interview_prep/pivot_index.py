def getPivotIndexUgly(array):
	if array == []:
		return -1
	if len(array) == 1:
		return 0
	for i in range(len(array)-1):
		if sum(array[:i]) == sum(array[i+1:]):
			return i
	return -1

def getPivotIndex(array):
	if array == []:
		return -1
	if len(array) == 1:
		return 0
	pivot_index = -1
	sum_start = sum_end = i = 0
	j = len(array) - 1
	last_i = True
	while i < j:
		if sum_start > sum_end:
			sum_end += array[j]
			j -= 1
			last_i = False
		else:
			sum_start += array[i]
			i += 1
			last_i = True
		if (last_i and i == j and sum_start == sum_end) or (i == j - 1 and sum_start == sum_end):
			return i
	return -1



a = [1,2,3,4,0,6]
a = [3,2,7,5]
# a = []
# a = [1]
# a = [1,2]
print getPivotIndex(a)