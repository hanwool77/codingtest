from collections import deque
import sys
input = lambda :sys.stdin.readline().rstrip()

N, K = map(int, input().split())    # N: 수빈이의 현재 점, K: 동생의 점

visited = [0] * 100001

q = deque()
q.append(N)


while q:
    now = q.popleft()
    if now == K:
        break

    for next in [now - 1, now + 1, now * 2]:
        if 0 <= next <= 100000 and visited[next] == 0:
            visited[next] = visited[now] + 1
            q.append(next)

print(visited[K])