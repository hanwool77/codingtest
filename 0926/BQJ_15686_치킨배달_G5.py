import sys
from itertools import combinations

input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
house = []
chicken = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

result = int(1e9)
for data in combinations(chicken, m):
    chicken_distance = 0
    for hx, hy in house:
        min_cd = int(1e9)
        for cx, cy in data:
            min_cd = min(min_cd, abs(hx - cx) + abs(hy - cy))
        chicken_distance += min_cd
    result = min(result, chicken_distance)

print(result)