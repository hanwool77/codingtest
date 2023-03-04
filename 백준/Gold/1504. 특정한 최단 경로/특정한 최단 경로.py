import sys, heapq
input = lambda :sys.stdin.readline().rstrip()


INF = int(1e9)
N, E = map(int, input().split())    # N: 정점의 개수, E: 간선의 개수
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

u, v = map(int, input().split())    # 반드시 지나야 하는 임의의 정점

def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)
    distance[start] = 0

    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for next, c in graph[now]:
            cost = distance[now] + c
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

    return distance

# 1 -> u -> v -> N번째 정점
case1 = dijkstra(1)[u] + dijkstra(u)[v] + dijkstra(v)[N]
# 1 -> v -> u -> N번째 정점
case2 = dijkstra(1)[v] + dijkstra(v)[u] + dijkstra(u)[N]

case = min(case1, case2)
print(case if case < INF else -1)