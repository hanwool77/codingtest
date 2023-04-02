import sys

input = lambda :sys.stdin.readline().rstrip()

n = int(input())    # n: 도시의 개수 ( 2 <= n <= 100)
m = int(input())    # m: 버스의 개수

INF = int(1e9)

graph = [[INF] * (n + 1)  for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] < INF:
            print(graph[i][j], end = ' ')
        else:
            print(0, end = ' ')
    print()