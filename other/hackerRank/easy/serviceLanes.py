cases = int(raw_input().split(' ')[1])

width = map(int, raw_input().split(' '))

for _ in range(cases):
    points = map(int, raw_input().split(' '))
    bike, car, truck = True, True, True
    for x in width[points[0]:points[1] + 1]:
        if x == 1:
            car, truck = False, False
        elif x == 2:
            truck = False
    if truck:
        print 3
    elif car:
        print 2
    else:
        print 1
