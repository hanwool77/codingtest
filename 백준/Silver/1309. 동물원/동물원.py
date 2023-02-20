import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())    # N <= 100,000

dp = [0] * (N + 1)  # dp[N] : N x 2 우리일 때 사자를 넣을 수 있는 경우의 수
dp[0] = 1
dp[1] = 3

if N >= 2:
    for i in range(2, N + 1):
        dp[i] = (2 * (dp[i - 1]) + dp[i - 2]) % 9901

print(dp[N])