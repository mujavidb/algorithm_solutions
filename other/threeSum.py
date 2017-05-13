def threeSum(array, val=0):
    results = []
    array.sort()
    for i in xrange(0,n - 2):
        a = array[i]
        start = i + 1
        end = len(array) - 1
        while start < end:
            b = array[start]
            c = array[end]
            if a + b + c == val:
                results.append([a,b,c])
                start += 1
                end -= 1
            elif a + b + c > val:
                end -= 1
            else:
                start += 1
    # unique = []
    # for x in results:
    #     if x not in unique:
    #         unique.append(x)
    unique = set()
    for x in results:
        unique.add(str(x))

    return [eval(x) for x in unique]