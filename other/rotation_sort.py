# Enter your code here. Read input from STDIN. Print output to STDOUT
#12354
#1,6,5,2,4,3
#165243 
#126354
#123564
#123456
#321 132

#rotate function that rotates from an index a certain number of times
#mark sorted index
#find smallest number
#if difference between sorted and unsorted is less than 3 print NO
#else rotate

def rotate(array, startIndex, factor):
	for _ in xrange(factor):
		try:
			a = array[startIndex]
			array[startIndex] = array[startIndex+1]
			array[startIndex+1] = array[startIndex+2]
			array[startIndex+2] = a
		except IndexError:
			print "E"
	print 
	return array

def rotation_sortable(numberList):
	iSorted = -1
	length = len(numberList)
	available = length - (iSorted + 1)
	while available >= 3:
		nextMin = numberList[iSorted:].index(min(numberList[iSorted:])) + iSorted
		temp = numberList[iSorted + 1]
		print nextMin
		
		if nextMin - iSorted > 3:
			print "{0} _ {1} - s({2}) - f({3})".format(iSorted, numberList, nextMin - 2, 2)
			numberList = rotate(numberList, nextMin - 2, 2)
		else:
			print "{0} _ {1} - s({2}) - f({3})".format(iSorted, numberList, iSorted + 1, nextMin - (iSorted + 1))
			numberList = rotate(numberList, iSorted + 1, nextMin - (iSorted + 1))
			if numberList[iSorted + 1] <= temp:
				iSorted +=1

		available = length - (iSorted + 1)

	if available == 0:
		return "YES"
	else:
		return "NO"

print rotation_sortable([1,6,5,2,4,3])