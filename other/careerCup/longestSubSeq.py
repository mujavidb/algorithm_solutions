# Find out the longest repeated common sub-string(overlapped) in a string.
# For example:- mystr = banana # The "ana" is the common overlapped sub-string is been used 2 times.

def isPalindrome(string):
    for i in xrange(int(len(string) / 2)):
        if string[i] != string[(i + 1) * -1]:
            return False
    return True

def longestSubSeq(string):
    longest = 0
    subSeq = ""
    stringLength = len(string) - 1
    for i in xrange(stringLength):
        for j in xrange(stringLength + 1, i - 1, -1):
            if isPalindrome(string[i:j]):
                print [i, j]
                subLen = len(string[i:j])
                if subLen % 2 == 0 and subLen / 2 > longest:
                    longest = subLen / 2
                    subSeq = string[i:j][0:subLen/2]
                elif (subLen + 1) / 2 > longest:
                    longest = (subLen + 1) / 2
                    subSeq = string[i:j][0:(subLen + 1)/2]
    print longest
    print subSeq

longestSubSeq("banana")
