import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())    # n: 정점의 개수, m: 간선의 개수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1) # 방문 체크 여부

def dfs(now):
    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            dfs(next)

ans = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)