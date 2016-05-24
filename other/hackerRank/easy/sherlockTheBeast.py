for _ in range(int(raw_input())):
    x = int(raw_input())
    multiple = x - (x % 3)
    while (x - multiple) % 5 != 0 and multiple >= 0:
        multiple -= 3
    if multiple < 0 or multiple % 3 != 0 or (x - multiple) % 5 != 0:
        print -1
    else:
        print ("5" * multiple) + ("3" * (x - multiple))
