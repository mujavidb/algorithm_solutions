# Given an integer x and an array y, create a 
# function that returns true if x exists as a sum of any contiguous elements in y.

# x, y
# 5, [4,3,2,3,1,5,0,7,8,4,5,2,3,6,0]

def contig_sum(x,y):
    length = len(y) - 1
    for i in range(len(y)):
        if i < length:
            value = y[i] + y[i+1]
            j = 2
            while value < x and (i + j) < length:
                value += y[i+j]
                j +=1
            if value == x:
                return True
    return False

print contig_sum(5, [4,3,2,3,1,5,0,7,8,4,5,2,3,6,0])
print contig_sum(5, [3,0])
