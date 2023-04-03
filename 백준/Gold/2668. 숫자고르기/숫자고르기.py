import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[int(input())].append(i)

result = []

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    q = deque()
    q.append(i)
    visited[i] = True

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                q.append(nx)
            elif visited[nx] and nx == i:
                result.append(i)

result.sort()
print(len(result))
for r in result:
    print(r)
