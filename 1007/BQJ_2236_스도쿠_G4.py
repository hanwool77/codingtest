import sys
arr = [list(map(int, input())) for _ in range(9)]

def checkRow(x, num):
    for i in range(9):
        if arr[x][i] == num:
            return False
    return True

def checkCol(y, num):
    for i in range(9):
        if arr[i][y] == num:
            return False
    return True

def checkMatrix(x, y, num):
    sx = x // 3 * 3
    sy = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if arr[sx + i][sy + j] == num:
                return False
    return True


zero = []
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            zero.append((i, j))

n = len(zero)

def sudoku(idx):
    if idx == n:
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end = '')
            print()
        sys.exit()

    x, y = zero[idx]

    for i in range(1, 10):
        if checkRow(x, i) and checkCol(y, i) and checkMatrix(x, y, i):
            arr[x][y] = i
            sudoku(idx + 1)
            arr[x][y] = 0


sudoku(0)