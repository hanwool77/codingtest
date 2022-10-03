import sys
input = lambda :sys.stdin.readline().rstrip()

N, K = map(int, input().split())
data = [(0, 0)]

for _ in range(N):
    a, b = map(int, input().split())    # a:무게, b: 가치
    data.append((a, b))

dp = [[0] * (K+1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(1, K + 1):
        if w >= data[i][0]:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - data[i][0]] + data[i][1])
        else:
            dp[i][w] = dp[i - 1][w]

print(dp[N][K])