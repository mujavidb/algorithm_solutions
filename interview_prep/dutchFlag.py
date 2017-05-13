# def naiiveDutch(array):
#     L = M = H = []
#     for x in array:
#         temp = getCategory(x)
#         if temp == 0:
#             L.append(x)
#         elif temp == 1:
#             M.append(x)
#         elif temp == 2:
#             H.append(x)
#     return L + M + H

# def naiiveDutchClean(array):
#     store = {}
#     store[0] = store[1] = store[2] = []
#     for x in array:
#         store[getCategory(x)].append(x)
#     return store[0] + store[1] + store[2]

def dutchMe(array):
    i = start = 0
    high = len(array) - 1
    while i <= high:
        if array[i] == 0:
            array[start],array[i]  = array[i], array[start]
            start += 1
            i += 1
        elif array[i] == 1:
            i += 1
        elif array[i] == 2:
            array[i], array[high] = array[high], array[i]
            high -= 1
    return array

print dutchMe([1,2,0,1,2,1,0,0,1,2,2])
print dutchMe([0,1,2,2,2,1,0,0,1,0,2])
print dutchMe([0,1])
print dutchMe([])
print dutchMe([0])
print dutchMe([2])
print dutchMe([0,2])
print dutchMe([1,2])
