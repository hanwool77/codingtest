T = int(input())

for t in range(1, T + 1):
    ans = 0
    day, mon, mon3, year = map(int, input().split())
    array = [0] + list(map(int, input().split()))

    dp = [0] * 13

    for i in range(1, 13):
        # 하루권
        a = dp[i - 1] + array[i] * day
        # 한달권
        b = dp[i - 1] + mon
        dp[i] = min(a, b)
        # 3달권
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + mon3)
        # 1년권
        if i >= 12:
            dp[i] = min(dp[i], dp[i - 12] + year)


    print(f"#{t} {dp[12]}")