import sys

input = lambda :sys.stdin.readline().rstrip()

N = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[N])

