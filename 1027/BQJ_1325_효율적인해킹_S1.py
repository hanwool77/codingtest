from collections import deque
import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(x):
    cnt = 1
    visited = [False] * (n + 1)
    q = deque()
    visited[x] = True
    q.append(x)

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                cnt += 1
                q.append(next)
    return cnt

max_value = -1
ans = []
for i in range(1, n + 1):
    hack_count = bfs(i)
    if hack_count >= max_value:
        max_value = hack_count
        ans.append((i, hack_count))

for idx, cnt in ans:
    if cnt == max_value:
        print(idx, end = ' ')