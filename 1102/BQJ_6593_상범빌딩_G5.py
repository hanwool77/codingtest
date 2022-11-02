import sys
from collections import deque

input = lambda :sys.stdin.readline().rstrip()
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 0, 1, 0]
dz = [0, 0, 0, 1, 0, -1]


def bfs():
    q = deque()
    q.append((sx, sy, sz))

    while q:
        x, y, z = q.popleft()
        if build[x][y][z] == 'E':
            break
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if build[nx][ny][nz] == '#':
                    continue
                else:
                    if visited[nx][ny][nz] == 0:
                        visited[nx][ny][nz] = visited[x][y][z] + 1
                        q.append((nx, ny, nz))


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    build = [[] * R for _ in range(L)]
    for i in range(L):
        for j in range(R):
            build[i].append(list(input()))
        input()
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if build[i][j][k] == 'S':
                    sx, sy, sz = i, j, k
                elif build[i][j][k] == 'E':
                    ex, ey, ez = i, j, k
    bfs()
    if visited[ex][ey][ez] == 0:
        print("Trapped!")
    else:
        print(f"Escaped in {visited[ex][ey][ez]} minute(s).")