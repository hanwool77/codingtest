import sys
import heapq
input = lambda :sys.stdin.readline().rstrip()

N, M = map(int, input().split())    # N: 헛간의 개수, M: 길의 개수(양방향)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = 987654321
distance = [INF] * (N + 1) # 1에서 각 헛간까지의 여물의 총합
distance[1] = 0
q = []
heapq.heappush(q, (0, 1))

while q:
    dist, now = heapq.heappop(q)
    if dist < distance[now]:
        continue

    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0],))

print(distance[N])

