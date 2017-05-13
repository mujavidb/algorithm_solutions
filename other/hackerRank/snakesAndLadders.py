raw_input()
ladders = [ map(int, raw_input().split(' ')) for _ in range(int(raw_input()))]
snakes = [ map(int, raw_input().split(' ')) for _ in range(int(raw_input()))]
shortcuts = [0] * 101

for x, y in ladders:
    shortcuts[x + 1] = y

for x, y in snakes:
    shortcuts[x + 1] = y

gameBoard = [[0] * 7] * 101

for i in range(1, 101):
    gameBoard[i][0] = i
    for j in range(1, 7):
        if shortcuts[i + j] != 0:
            gameBoard[i][j] = shortcuts[i + j]
        else:
            if i + j > 100:
                gameBoard[i][j] = i
            else:
                gameBoard[i][j] = i + j
    print gameBoard[i]
print "love"
