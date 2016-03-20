def int_pairs(array, x):
	for a in range(len(array)):
	    for b in array[a + 1:]:
	        if array[a] + b == x:
	            print str(array[a]) + " - " + str(b) + ", ",

def int_pairs_two(array, x):
    for a in range(len(array)):
        test = x - array[a]
        for b in array[a + 1:]:
            if b == test: 
                print str(array[a]) + " - " + str(b) + ", ",

def recursive_pairs(array, x):
	if not array:
		return
	for a in range(1,len(array)):
		if array[0] + array[a] == x: 
			print str(array[0]) + " - " + str(array[a]) + ", ",
	recursive_pairs(array[1:], x)


int_pairs([4,5,6,2,1,3,4,8,9,6,0], 9)
print 
int_pairs_two([4,5,6,2,1,3,4,8,9,6,0], 9)
print
recursive_pairs([4,5,6,2,1,3,4,8,9,6,0], 9)