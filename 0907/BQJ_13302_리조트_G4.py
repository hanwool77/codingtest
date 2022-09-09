n, m = map(int, input().split())
no_resort = list(map(int, input().split()))
coupon_count = int(n / 5)
INF = 1e9

dp = [[INF] * (coupon_count + 5) for _ in range(n + 1)]   # i번째 날 j개의 쿠폰을 갖고 있을 때 최소 리조트 비용

dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(coupon_count + 1):
        if dp[i - 1][j] == INF:
            continue
        if i not in no_resort:  # 리조트 사용
            if j >= 3:  # 쿠폰 사용
                dp[i][j] = dp[i-1][j-3]

            # 1일권
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 10000)

            # 3일권
            if i >= 3:
                dp[i][j + 1] = min(dp[i-3][j] + 25000, dp[i][j + 1])

            # 5일권
            if i >= 5:
                dp[i][j + 2] = min(dp[i-5][j] + 37000, dp[i][j + 2])

        else:   # 리조트 사용 x
            dp[i][j] = dp[i-1][j]

print(dp)