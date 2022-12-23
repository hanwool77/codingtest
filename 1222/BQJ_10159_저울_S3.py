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
            continue
        if graph[i][j] == INF and graph[j][i] == INF:   # i에서 j로도 갈 수 없고 j에서도 i로 갈 수 없으면 서로 무게 비교 불가
            result += 1
    print(result)