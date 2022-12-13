import sys
input = lambda :sys.stdin.readline().rstrip()

N, M = map(int, input().split())    # N: 도시의 개수, M: 도로의 개수
전체예산 = 0
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    전체예산 += c
    edges.append((c, a, b))

edges.sort()
parent = [i for i in range(N + 1)]

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

예산 = 0
n = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        예산 += cost
        n += 1

print(전체예산 - 예산) if n == N-1 else print(-1)