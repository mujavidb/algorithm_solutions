# Given a string "2-4a0r7-4k", there are two dashes which we can split into 3 groups of length 1, 5, 2. 

# If we want each group to be length 4, then we get "24A0-R74k" 

# Given a String A and an int K, return a correctly formatted string. 

# IF A is "2-4A0r7-4k" and B is 4, string is "24A0-R74K" 
# IF K is 3, string is "24-A0R-74K" as the first grp could be shorter.

def dashSplit(string, dashes):
	string = string.replace("-", "")
	string = list(string)
	for i in range(len(string) - dashes, 0, -dashes):
	    string.insert(i, "-")
	string = "".join(string)
	return string

print dashSplit("2-4a0r7-4k", 4)
print dashSplit("2-4a0r7-4k", 3)