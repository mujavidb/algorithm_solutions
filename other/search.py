def binSearch(array, value, start, end):
	mid = (start + end) / 2
	if array[mid] == value:
		return mid
	if start + 1 >= end:
		return -1
	if array[mid] > value:
		return binSearch(array, value, start, mid)
	else:
		return binSearch(array, value, mid, end)

value = 12
array = [1,2,4,6,7,8,9]
       # 0 1 2 3 4 5 6
print binSearch(array, value, 0, len(array) - 1)