import sys
from collections import deque

input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((0, 0))
visited[0][0] = True

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print(graph[n - 1][m - 1])
