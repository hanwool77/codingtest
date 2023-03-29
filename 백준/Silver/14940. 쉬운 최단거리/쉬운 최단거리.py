import sys
from collections import deque

input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())    # n: 세로, m: 가로

graph = [list(map(int, input().split())) for _ in range(n)] # 지도 입력받기
visited = [[False] * m for _ in range(n)]   # 방문 체크 여부

sx, sy = 0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            sx, sy = i, j # 출발지
        elif graph[i][j] == 1:
            graph[i][j] = -1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((sx, sy))
graph[sx][sy] = 0
visited[sx][sy] = True

while q:
    cx, cy = q.popleft()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] == -1:  # 한번도 방문하지 않았고 갈 수 있는 땅이면
                graph[nx][ny] = graph[cx][cy] + 1
                visited[nx][ny] = True
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        print(graph[i][j], end = ' ')
    print()


