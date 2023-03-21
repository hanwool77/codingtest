import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

N, K = map(int, input().split())   # N: 수빈, K: 동생
distance = [-1] * 100001    # 처음에는 모든 지점 방문X
distance[N] = 0 # 현재 수빈이가 있는 위치는 방문했다고 표시

q = deque()
q.append(N)

cnt = 0

while q:
    now = q.popleft()
    if now == K:
        cnt += 1

    for next in [now - 1, now + 1, now * 2]:
        if 0 <= next < 100001:
            if distance[next] == -1 or distance[next] == distance[now] + 1:
                distance[next] = distance[now] + 1
                q.append(next)



print(distance[K])
print(cnt)