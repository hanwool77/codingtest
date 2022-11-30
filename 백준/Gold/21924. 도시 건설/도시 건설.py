import sys

input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())    # n: 건물의 개수, m: 도로의 개수
edges = []
total_cost = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    total_cost += c
    edges.append((c, a, b))

edges.sort()
parent = [i for i in range(n + 1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
건물 = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        건물 += 1

if n - 1 == 건물:
    print(total_cost - result)
else:
    print(-1)

