import sys
import heapq
input = lambda :sys.stdin.readline().rstrip()

INF = int(1e9)
V, E = map(int, input().split())    # V: 정점의 개수, E: 간선의 개수
K = int(input())    # 시작 정점의 개수
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v (가중지 w)
    graph[u].append((v, w))

distance = [INF] * (V + 1)  # distance[N]: 정점 K에서 N까지의 가중치
distance[K] = 0

q = []
heapq.heappush(q, (0, K))

while q:
    c, now = heapq.heappop(q)
    if distance[now] < c:
        continue

    for next, nc in graph[now]:
        cost = c + nc
        if cost < distance[next]:
            distance[next] = cost
            heapq.heappush(q, (cost, next))

for i in range(1, V + 1):
    print(distance[i] if distance[i] != INF else "INF")
