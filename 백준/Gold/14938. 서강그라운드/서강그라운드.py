import sys

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)

n, m, r = map(int, input().split())  # n: 지역의 개수, m: 수색 범위, r: 길의 개수
graph = [[INF] * (n + 1) for _ in range(n + 1)]
data = [0] + list(map(int, input().split()))
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n + 1):
    item = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            item += data[j]
    if result < item:
        result = item

print(result)
