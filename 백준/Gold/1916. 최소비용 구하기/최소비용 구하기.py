import sys
import heapq
input = lambda :sys.stdin.readline().rstrip()

n = int(input())    # 도시의 개수
m = int(input())    # 버스의 개수

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, d in graph[now]:
            cost = dist + d
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

dijkstra(start)
print(distance[end])