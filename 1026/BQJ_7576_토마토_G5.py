from collections import deque
import sys

input = lambda :sys.stdin.readline().rstrip()

m, n = map(int, input().split())
graph = []

tomato = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
all_riped = True

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            tomato.append((i, j))
        if graph[i][j] == 0:
            all_riped = False

if all_riped:
    print(0)
    sys.exit()

q = deque(tomato)
while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

ans = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            sys.exit()
        if ans < graph[i][j]:
            ans = graph[i][j]

print(ans - 1)