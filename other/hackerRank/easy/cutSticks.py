raw_input()
width = map(int, raw_input().split(' '))
while width:
    print len(width)
    lowestVal = min(width)
    i = 0
    while i < len(width):
        width[i] -= lowestVal
        if width[i] <= 0:
            width.pop(i)
        else:
            i += 1
