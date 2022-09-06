from collections import deque

n, k = map(int, input().split())

array = [i for i in range(1, n + 1)]
q = deque(array)

res = list()

while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    res.append(q.popleft())

ans = '<'
for r in res:
    ans += str(r) + ', '

ans = ans[:len(ans) - 2]
print(ans + '>')
