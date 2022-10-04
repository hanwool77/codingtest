import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
empty = []
virus = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))    # 빈칸인 곳
        elif graph[i][j] == 2:
            virus.append((i, j))    # 바이러스 인 곳


def spread(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if map[nx][ny] == 0:
                    map[nx][ny] = 2
                    q.append((nx, ny))


def check_safe():
    cnt = 0
    for i in range(n):
        for j in range(m):
           if map[i][j] == 0:
               cnt += 1
    return cnt


for data in combinations(empty, 3):
    map = deepcopy(graph)
    for x, y in data:
        map[x][y] = 1   # 빈칸인 곳 중 벽 세우기

    for vx, vy in virus:
        spread(vx, vy)  # 바이러스 퍼트리기

    result = max(result, check_safe())

print(result)