from collections import deque
import sys
input = lambda :sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())

visited = [[False] * 201 for _ in range(201)]
q = deque()
visited[0][0] = True
q.append((0, 0))
ans = []

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

while q:
    x, y = q.popleft()  # x: a비커에 담긴 물의 양, y: b비커에 담긴 물의 양
    z = c - x - y   # z: c비커에 담긴 물의 양

    if x == 0:
        ans.append(z)

    # x -> y로 물 옮기기
    water = min(x, b - y)
    pour(x - water, y + water)

    # x -> z로 물 옮기기
    water = min(x, c - z)
    pour(x - water, y)

    # y -> x로 물 옮기기
    water = min(a - x, y)
    pour(x + water, y - water)

    # y -> z로 물 옮기기
    water = min(y, c - z)
    pour(x, y - water)

    # z -> x로 물 옮기기
    water = min(z, a - x)
    pour(x + water, y)

    # z -> y로 물 옮기기
    water = min(b-y, z)
    pour(x, y + water)

ans.sort()
for a in ans:
    print(a, end = ' ')