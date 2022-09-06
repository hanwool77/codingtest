from collections import deque
import sys

input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())    # 1 <= n, m <= 300  교실: n x m
x1, y1, x2, y2 = map(int, input().split())  # 주난이의 위치 x1,y1  범인의 위치 x2,y2

graph = [list(input()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

distance = [[1e9] * m for _ in range(n)]
distance[x1-1][y1-1] = 0

q = deque()
q.append((x1-1, y1-1))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == '0':
                if distance[x][y] < distance[nx][ny]:
                    distance[nx][ny] = distance[x][y]
                    q.append((nx, ny))
            elif graph[nx][ny] == '1':
                if distance[x][y] + 1 < distance[nx][ny]:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
            elif graph[nx][ny] == '#':
                if distance[x][y] + 1 < distance[nx][ny]:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

print(distance[x2-1][y2-1])