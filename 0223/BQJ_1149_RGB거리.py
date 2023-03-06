import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
color = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    r, g, b = map(int, input().split())
    color[i][0] = r
    color[i][1] = g
    color[i][2] = b

dp = [[0] * 3 for _ in range(N + 1)]   # dp[i][0] -> i번째 집을 R로 칠할 경우, dp[i][1] -> i번째 집을 G로 칠할 경우, dp[i][2] -> i번째 집을 B로 칠할 경우
dp[1][0] = color[1][0]
dp[1][1] = color[1][1]
dp[1][2] = color[1][2]

for i in range(2, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + color[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + color[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + color[i][2]

print(min(dp[N]))
