import heapq
import sys

input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
INF = int(1e9)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [INF] * (n + 1)
distance[0] = 0

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))

dijkstra(1)
num = 0
dis = 0

for i in range(1, n + 1):
    if distance[i] > dis:
        dis = distance[i]
        num = i

print(num, dis, distance.count(dis))

