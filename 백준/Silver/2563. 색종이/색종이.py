import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())    # 색종이의 수
graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    r, c = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if graph[r + i][c + j] == 0:
                graph[r + i][c + j] = 1

ans = 0
for i in range(101):
    ans += sum(graph[i])

print(ans)
