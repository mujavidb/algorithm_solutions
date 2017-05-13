chapters, maxItems = map(int, raw_input().split(' '))
itemsPerChapter = map(int, raw_input().split(' '))
pageNumber = 1
cSpecial = 0
for i in range(chapters):
    remainder = itemsPerChapter[i] % maxItems
    pagesInChapter = int(itemsPerChapter[i] / maxItems) + remainder
    mini = 1
    maxi = maxItems
    if itemsPerChapter[i] < maxItems:
        maxi = itemsPerChapter[i]
    for j in range(pagesInChapter):
        newNum = pageNumber + j
        if newNum >= mini and newNum <= maxi:
            cSpecial += 1
            print "minimum: {}, maximum: {}, pageNumber: {}".format(mini, maxi, newNum)
        mini += maxItems
        maxi += maxItems
        if (maxItems * (j + 1)) + remainder > maxi:
            maxi = (maxItems * (j + 1)) + remainder
    pageNumber += pagesInChapter

print cSpecial
