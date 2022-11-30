import sys
input=lambda :sys.stdin.readline().rstrip()

n, m, t = map(int, input().split()) # N: 도시의 개수, M: 도로의 개수, T: 도로 비용
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

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

edges.sort()
answer = 0
line = 0
비용 = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost
        answer += 비용
        비용 += t
        line += 1
    if line == n - 1:
        break

print(answer)
