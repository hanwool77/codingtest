import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

def dfs(x):
    print(x, end = ' ')
    for nx in graph[x]:
        if not visited_dfs[nx]:
            visited_dfs[nx] = True
            dfs(nx)

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        print(x, end = ' ')
        for nx in graph[x]:
            if not visited_bfs[nx]:
                visited_bfs[nx] = True
                q.append(nx)

visited_dfs[V] = True
visited_bfs[V] = True
dfs(V)
print()
bfs(V)

