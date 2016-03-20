#Design an algorithm and write code to remove the duplicate characters 
#in a string without using any additional buffer. NOTE: One or two additional
#variables are fine. An extra copy of the array is not.

#1234456
#123456

#111234456
#123456

#ababb
#abab

def removeDups(string):
	length = len(string)
	i = 0
	removals = 0
	while i < length and (i + 1 + removals) != length:
		if string[i] == string[i+1]:
			del string[i]
			removals +=1
			continue
		i +=1
	return string

print removeDups(["1","1","1","2","3","4","5"])
print removeDups(["1","1","1","2","3","4","4","4","5"])
print removeDups(["a","b","a","a","b","d","e","e","d"])