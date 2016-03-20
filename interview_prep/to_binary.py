# # Given to binary numbers(as strings) return sum of both(also in binary)

def binary(n):
    string = ""
    while n > 0:
        if n % 2:
            string = "1" + string
        else:
            string = "0" + string
        n //= 2
    return string if string else "0"

x = "111100010"
y = "10100"

def add(x,y):
        maxlen = max(len(x), len(y))

        x = x.zfill(maxlen)
        y = y.zfill(maxlen)

        result = ''
        carry = 0

        for i in range(maxlen-1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0

            # r can be 0,1,2,3 (carry + x[i] + y[i])
            # and among these, for r==1 and r==3 you will have result bit = 1
            # for r==2 and r==3 you will have carry = 1

            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1       

        if carry !=0 :
            result = '1' + result

        print result

def bin_add(*args): 
    return bin(sum(int(x, 2) for x in args))[2:]

add(x, y)
print bin(int(x,2) + int(y,2))[2:]