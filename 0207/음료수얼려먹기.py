import sys

input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
            dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 0:
            dfs(i, j)
            ans += 1

print(ans)