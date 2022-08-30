# 백준 16953
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())  # 1 <= a, b <= 10^9
res = -1

q = deque()
q.append((a, 1))

while q:
    a, cnt = q.popleft()

    if a == b:
        res = cnt
        break

    if a * 2 <= b:
        q.append((a*2, cnt + 1))
    if a * 10 + 1 <= b:
        q.append((a * 10 + 1, cnt + 1))

print(res)