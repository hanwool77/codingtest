import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, N + 1):
    result = 0
    for j in range(1, N + 1):
        if i == j:
            result += 1
            continue
        if graph[i][j] != INF or graph[j][i] != INF:
            result += 1
    print(N - result)