import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

cnt = 0
max_area = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    area = 1
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and array[nx][ny] == 1:
                area += 1
                visited[nx][ny] = True
                q.append((nx, ny))

    return area

for i in range(n):
    for j in range(m):
        if not visited[i][j] and array[i][j] == 1:
            max_area = max(max_area, bfs(i, j))
            cnt += 1

print(cnt)
print(max_area)