import sys
input = lambda :sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())    # 동전의 가지 수
    coin = list(map(int, input().split()))
    M = int(input())    # 동전으로 만들어야 할 금액

    dp = [0] * (M + 1)
    dp[0] = 1

    for c in coin:
        for i in range(c, M + 1):
            dp[i] += dp[i - c]
    print(dp[M])