testCase = "cba"
totalOperations = 0

for i in xrange(len(testCase)/2):
    leftVal = ord(testCase[i])
    rightVal = ord(testCase[-(i + 1)])
    totalOperations += (max(rightVal, leftVal) - min(rightVal, leftVal))

print totalOperations
