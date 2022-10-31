import heapq
import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())    # 도시의 개수 1<= N <= 1,000
M = int(input())    # 버스의 개수 1 <= M <= 100,000
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())  # 출발점, 도착점
INF = int(1e9)
distance = [INF] * (N + 1)

def dijkstra(start):
    q = []
    distance[start] = 0
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

dijkstra(start)
print(distance[end])
