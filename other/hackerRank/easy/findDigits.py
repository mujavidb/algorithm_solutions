for _ in range(int(raw_input())):
    n = int(raw_input())
    count = 0
    for x in str(n):
        if int(x) != 0 and n % int(x) == 0:
            count += 1
    print count
