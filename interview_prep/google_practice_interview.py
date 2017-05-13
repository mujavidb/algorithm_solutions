#[1, 2, 3, 3, 3, 3, 3, 3, 1] indices = 2, 3

import random
def equalMax(array, k):
    currentMax = -float("inf")
    maxCount = 0
    maxes = []
    for i in range(len(array)):
        if array[i] > currentMax:
            currentMax = array[i]
            maxCount = 1
            maxes = [i]
        elif array[i] == currentMax:
            maxCount += 1
            if len(maxes) == k:
                if random.random() < k/maxCount:
                    maxes[rand(0,k - 1)] = i
            else:
                maxes.append(i)
    return maxes

maxCount

k/maxCount

[1, 1, 1, 1, 1, 1, 1, 1,1, 1], k=4 O(k) space

P(1st) = 1 * 1/2 * 2/3 * 3/4 = 1/4
P(2nd) = 1/2 * 2/3 * 3/4 = 1/4
P(3rd) = 1/3 * 3/4 = 1/4
P(4th) = 1/4


-always ask clarifying/edge case questions
-check before claiming correct