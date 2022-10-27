import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
top = defaultdict(deque)

for i in range(1, 5):
    top[i] = deque(list(map(int, input())))

k = int(input())
for _ in range(k):
    n, dir = map(int, input().split())  # n: 번호, dir: 방향

    rotate = [False] * 5
    rotate[n] = True

    for right in range(n + 1, 5):
        if top[right][6] != top[right - 1][2]:
            rotate[right] = True
        else:
            break
    for left in range(n - 1, 0, -1):
        if top[left][2] != top[left + 1][6]:
            rotate[left] = True
        else:
            break

    for i in range(1, 5):
        if rotate[i]:
            if (n + i) % 2 == 0:
                top[i].rotate(dir)
            else:
                top[i].rotate(-dir)


ans = 0
score = 1

for i in range(1, 5):
    if top[i][0] == 1:
        ans += score
    score *= 2

print(ans)
