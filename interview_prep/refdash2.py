#- A magic index in an array A[1...n-1]
# is defined to be an index such that A[i]=i.
#Given an array of distinct integers,
#find the magic index if one exists in the array.


#- What if the array is sorted and all integers are distinct?


#[-1,0,1,2,3,4,5,7,10]


#[-40, -20, -1, 1, 2, 3, 5, 7, 9, 11, 13]
# 0     1   2   3  4  5  6  7  8   9  10 : indices

#when the midpoint is checked, 
#    if less than index, left can be disregarded
#    if greater than index, right can be disregarded
#    if equal, return index

s 6
e 8
m 7

def findMagicIndex(array):
    start = 0
    end = len(array) - 1
    mid = (start + end) / 2 
    while start < end:
        if array[mid] == mid:
            return mid
        if array[mid] < mid:
            start = mid
        elif array[mid] > mid:
            end = mid
        mid = (start + end) / 2 
    return -1

# - What if the array is sorted and all integers are not distinct?

# [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
#  0    1   2  3  4  5  6  7  8   9  10 : indices