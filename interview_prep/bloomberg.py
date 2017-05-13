# Bloomberg
# * Question 1
#     * [4, 2, 7, 5, 1, 9]
#     * find the maximum diff between two items in an array
# * Question 2
#     * given 2 string, find the min operations required to make them anagrams
# * Question 3
#     * given string, find longest palindromic substring

# Returns the zero based index of the first occurrence of any character of str2 in str1 
# Input: 
# str1="adf6ysh" 
# str2="123678" 

# output: 3 

def getIndex(str1, str2):
	if not str2 or not str1:
		return -1
	hashmap = {}
	for i in range(len(str1)):
		if hashmap.has_key(x):
			hashmap[x].append(i)
		else:
			hashmap[x] = [i]
	for j in range(len(str2)):
		if hashmap.has_key(str2[j]):
			return hashmap[str2[j]][0]
	return -1

# Given an unsorted integer array, place all zeros to the 
# end of the array without changing the sequence of non-zero 
# elements. (i.e. [1,3,0,8,12, 0, 4, 0,7] --> [1,3,8,12,4,7,0,0,0])

def quadraticShiftZeros(unsorted):
	for i in range(len(unsorted)):
		if unsorted[i] == 0:
			unsorted.append(0)
			del unsorted[i]
	return unsorted

def linearShiftZeros(unsorted):
	zeroCount = 0
	for i in xrange(len(unsorted)):
		if unsorted[i] == 0:
			zeroCount += 1
		else:
			unsorted[i - zeroCount] = unsorted[i]
		if zeroCount + i > len(unsorted):
			unsorted[i] = 0
	return unsorted

# Royal titles consist of name followed by space and a Roman numeral. Example: Richard IV. The Roman numeral in the title 
# can go to L (50). You are given the roman numerals from 1 to 10: 
# I II III IV V VI VII VIII IX X. And you are given the 10 multiples up to 50: XX XXX IL L. Numbers between 10 and 50 that 
# are not given can be formed from 10 multiples and a numeral b/w 1 and 9. Example: 48 is XLVIII wichi is XL (40) plus 
# VIII (8). 
# <p> 
# You are given an array of Roman titles sort it as follows: sort it on the name unless the names are equal, in which 
# case you have to sort it on the ordinal of the numerals. 
# Examples: 
# Henry II, Edward VIII => Eward VII, Henry II 
# Richard V, Richard II, Richard X => Richard II, Richard V, Richard X

def sortTitles(titles):
	titles.sort()
	return titles


# Given a string find biggest palindrome substring. For example for a 
# given string "AABCDCBA" output should be "ABCDCBA" and for given 
# string "DEFABCBAYT" output should be "ABCBA".

# space 1
# time nlogn
def longestSub(string):
	if not string:
		return 0
	if len(string) == 2 or (len(string) == 2 and string[0] == string[1]):
		return len(string)
	longest = 1
	for i in range(1, len(string)):
		cLongest = 1
		for j in range(1,i):
			if i-j >= 0 and i+j < len(string) and string[i-j] == string[i+j]:
				cLongest += 2
		longest = cLongest if cLongest > longest else longest
	return longest

# is valid bst
# 
def validate(root):
	return isValidBST(root, -float("inf"), float("inf"));
def isValidBST(root, minVal, maxVal):
	return (root == null) or /
			(root.data <= minVal or root.data >= maxVal) or /
			isValidBST(root.left, minVal, root.data) and /
			isValidBST(root.right, root.data, maxVal)

# 
# 
# validate(TreeNode root, int min, int max) {
# 	if (root == null) {
# 		return true;
# 	}
	
# 	if (root.data <= min || root.data >= max) {
# 		return false;
# 	}
	
# 	return validate(root.left, min, root.data) && validate(root.right, root.data, max);
# }

## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.

# A: 0:00 - 8:30, 9:15 - 10:00, 10:30 - 11:30 ...
     # [[1, 2], [3, 4], [5, 6]] - 3
# B: 0:00 - 9:00, 11:00 - 12:15 ...
# Duration: 60 min
# :00, :15, :30, :45

def firstAvailableTimeSlot(duration, A, B):
    i = j = 0
    freeSlots = []
    availableSlots = {}
    while i < len(A):
        currentSlot = []
        
        j += 1 if A[i][0] > B[j][1] else 0
        
        # compare start time of free slots
        if A[i][1] > B[j][1]:
            currentSlot.append(A[i][0])
        else:
            currentSlot.append(B[j][0])
            
        # compare end times
        if A[i+1][0] > B[j+1][0]:
            currentSlot.append(B[i+1][0])
        else:
            currentSlot.append(A[j+1][0])
        
        freeSlots.append(currentSlot)
        
        i += 1
        
    for slot in freeSlots:
        availableSlots[slot[0]] = slot[1]
    
    for time in range(0,24*60,15):
        if availableSlots.has_key(time):
            currentDuration = availableSlots[time] - time
            if currentDuration >= duration:
                return [time, availableSlots[time]]
    
    return []








