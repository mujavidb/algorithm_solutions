n = int(raw_input())
oldMatrix = [ map(int, list(raw_input())) for _ in range(n) ]
newMatrix = list(oldMatrix)
for y in range(1, n - 1):
    for x in range(1, n - 1):
        current = oldMatrix[x][y]
        if current > oldMatrix[x - 1][y] and current > oldMatrix[x + 1][y] and current > oldMatrix[x][y + 1] and current > oldMatrix[x][y - 1]:
            newMatrix[x][y] = "X"

for y in newMatrix:
    newStr = ""
    for x in y:
        newStr += str(x)
    print newStr
