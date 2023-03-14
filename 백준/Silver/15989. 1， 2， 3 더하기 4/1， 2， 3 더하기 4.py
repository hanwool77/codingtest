import sys
input = lambda :sys.stdin.readline().rstrip()

T = int(input())
num = [1, 2, 3]

for _ in range(T):
    n = int(input())
    dp = [0] * (10001)
    dp[0] = 1

    if n < 4:
        print(n)
        continue

    for x in num:
        for i in range(x, n + 1):
            dp[i] += dp[i - x]

    print(dp[n])