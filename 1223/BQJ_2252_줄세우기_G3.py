import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)    # 진입 차수

for _ in range(M):
    a, b = map(int, input().split())    # a가 b보다 키가 작음(앞에 섬)
    graph[a].append(b)
    indegree[b] += 1

q = deque() # 진입 차수가 0인 리스트
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

answer = []

while q:
    x = q.popleft()
    answer.append(x)

    for n in graph[x]:
        indegree[n] -= 1
        if indegree[n] == 0:
            q.append(n)

print(*answer)

