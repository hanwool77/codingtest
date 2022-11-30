import sys
sys.setrecursionlimit(10000)
input = lambda :sys.stdin.readline().rstrip()

T = int(input())    #  테스트 케이스 개수
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)


for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        j, i = map(int, input().split())
        graph[i][j] = 1   # 배추

    result = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                result += 1
                dfs(i, j)

    print(result)

