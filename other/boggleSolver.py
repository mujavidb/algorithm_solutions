# represent the graph
board = [['G','I','Z'],
         ['U','E','K'],
         ['Q','S','E']]

# recruisve method to iterate with each str (store in dictionary)

    # iterate through each letter
    # base case: if not adjacent nodes, then were done
    # recursive case, for each adjacent node, add that and recurse

def findWord(x,y,visited, acc):

    print acc

    # North
    if x > 0 and (str(x-1) + str(y)) not in visited:
        fun = visited.copy()
        fun.add((str(x-1) + str(y)))
        findWord(x-1, y, fun, acc + str(board[x-1][y]))

    # NorthEast
    if x > 0 and y < len(board[0]) - 1 and (str(x-1) + str(y + 1)) not in visited:
        fun = visited.copy()
        fun.add(str(x-1) + str(y + 1))
        findWord(x-1, y+1, fun, acc + str(board[x-1][y+1]))

    # NorthWest
    if x > 0 and y > 0 and (str(x-1) + str(y-1)) not in visited:
        fun = visited.copy()
        fun.add((str(x-1) + str(y-1)))
        findWord(x-1, y-1, fun, acc + str(board[x-1][y-1]))

    # East
    if y < len(board[0]) - 1 and (str(x) + str(y + 1)) not in visited:
        fun = visited.copy()
        fun.add(str(x) + str(y + 1))
        findWord(x, y+1, fun, acc + str(board[x][y+1]))

    # West
    if y > 0 and (str(x) + str(y - 1)) not in visited:
        fun = visited.copy()
        fun.add(str(x) + str(y - 1))
        findWord(x, y-1, fun, acc + str(board[x][y-1]))

    # South
    if x < len(board[0]) - 1 and (str(x+1) + str(y)) not in visited:
        fun = visited.copy()
        fun.add(str(x+1) + str(y))
        findWord(x+1, y, fun, acc + str(board[x+1][y]))

    # SouthEast
    if x < len(board[0]) - 1 and y < len(board[x]) - 1 and (str(x+1) + str(y+1)) not in visited:
        fun = visited.copy()
        fun.add(str(x+1) + str(y + 1))
        findWord(x+1, y+1, fun, acc + str(board[x+1][y+1]))

    # South West
    if x < len(board[0]) - 1 and y > 0 and (str(x+1) + str(y-1)) not in visited:
        fun = visited.copy()
        fun.add(str(x+1) + str(y-1))
        findWord(x+1, y-1, fun, acc + str(board[x+1][y-1]))

def printWords(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            test = set()
            test.add(str(x) + str(y))
            findWord(x,y, test, str(board[x][y]))

# print out all words
printWords(board)
print blob
