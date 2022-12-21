import sys
import heapq
input = lambda :sys.stdin.readline().rstrip()

N, D = map(int, input().split())
graph = [[] for i in range(D + 1)]

for i in range(D):
    graph[i].append((i + 1, 1))

for _ in range(N):
    start, end, dist = map(int, input().split())
    if end > D:
        continue
    graph[start].append((end, dist))

INF = int(1e9)
distance = [INF] * (D + 1)

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)
print(distance[D])
