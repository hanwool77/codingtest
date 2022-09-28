import sys
import heapq

input = lambda :sys.stdin.readline().rstrip()
INF = float('inf')
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

distance = [INF] * (n + 1)

def djikstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

djikstra(x)
result = []
no_city = True
for i in range(1, len(distance)):
    if distance[i] == k:
        result.append(i)
        no_city = False

if no_city:
    print(-1)
else:
    for r in result:
        print(r)
