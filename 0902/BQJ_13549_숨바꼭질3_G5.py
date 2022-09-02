from collections import deque

n, k = map(int, input().split())    # n: 나, k: 동생

q = deque()
q.append(n)
distance = [1e9] * 100001
distance[n] = 0

while q:
    x = q.popleft()
    # if x == k:
    #     break

    if 0 <= x * 2 <= 100000: # 2*x가 범위 내일 때
        if distance[x] < distance[x * 2]:
            distance[x * 2] = distance[x]
            q.appendleft(2*x)
    if 0 <= x + 1 <= 100000:     # x + 1이 범위 내일 때
        if distance[x] + 1 < distance[x + 1]:
            distance[x + 1] = distance[x] + 1
            q.append(x + 1)
    if 0 <= x - 1 <= 100000:
        if distance[x] + 1 < distance[x - 1]:
            distance[x - 1] = distance[x] + 1
            q.append(x - 1)


print(distance[k])

