# Length of longest subarray of sum less than or equal to k

def max_length(s, k): # These two mark the start and end of the subarray that current used to be. 
	start = end = total = 0
	maxLength = -1 # returns -1 if there is no subsequence that adds up to k.
	for i in s:
	    total += i
	    end += 1
	    while total > k: # Shrink the array from the left, until the sum is <= k.
	        total -= s[start]
	        start += 1
	    maxLength = max(maxLength, end - start)

	return maxLength