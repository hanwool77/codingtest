import sys
from collections import deque

N = int(input())    # 트리의 정점 개수
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)
ans = 0

q = deque()
q.append(1)

while q:
    node = q.popleft()
    if node != 1 and len(graph[node]) == 1:
        ans += visited[node]

    for next_node in graph[node]:
        if visited[next_node] == 0:
            visited[next_node] = visited[node] + 1
            q.append(next_node)

print('YES') if ans % 2 != 0 else print("NO")