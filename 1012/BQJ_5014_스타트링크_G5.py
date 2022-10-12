from collections import deque
import sys

input = lambda : sys.stdin.readline().rstrip()

# S:시작, G:목적
F, S, G, U, D = map(int, input().split())

arr = [0] * (F + 1)
visited = [False] * (F + 1)

q = deque()
q.append(S)
visited[S] = True

while q:
    x = q.popleft()
    if x == G:  # 목적지 도착했으면
        break

    for nx in [x + U, x - D]:
        if 1 <= nx <= F and not visited[nx]:
            arr[nx] = arr[x] + 1
            visited[nx] = True
            q.append(nx)

if S == G:
    print(0)
else:
    print(arr[G]) if arr[G] > 0 else print('use the stairs')
