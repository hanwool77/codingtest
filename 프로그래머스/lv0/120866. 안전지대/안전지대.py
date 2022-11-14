dx = [-1, -1, -1, 0, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, -1, 1, -1, 0, 1, 0]

def solution(board):
    n = len(board)
    safey = [[0] * n for _ in range(n)]
    answer = 0
    
    for x in range(n):
        for y in range(n):
            if board[x][y] != 1:
                continue
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    safey[nx][ny] += 1
    print(safey)
    for i in range(n):
        for j in range(n):
            if safey[i][j] == 0:
                answer += 1
    return answer