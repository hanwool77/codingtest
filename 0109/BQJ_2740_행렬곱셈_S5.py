import sys

input = lambda :sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())

for _ in range(M):
    B.append(list(map(int, input().split())))

result = [[0] * K for _ in range(N)]

for a in range(N):
    for b in range(K):
        for c in range(M):
            result[a][b] += A[a][c] * B[c][b]

for r in result:
    print(*r)