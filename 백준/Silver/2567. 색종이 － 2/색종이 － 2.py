import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())    # 색종이의 수
arr = [[0] * 102 for _ in range(102)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[a + i][b + j] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if arr[ni][nj] == 0:
                    ans += 1

print(ans)