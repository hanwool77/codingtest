import sys
input=lambda :sys.stdin.readline().rstrip()

T = int(input())

for t in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    swim = [0] + list(map(int, input().split()))   # 달마다 수영장 이용 날짜
    dp = [0] + [123456789] * 12
    for i in range(1, 13):
        # 하루권 사용
        dp[i] = min(dp[i], dp[i-1] + swim[i] * day)

        # 한달권 사용
        dp[i] = min(dp[i], dp[i - 1] + mon)

        # 3달권 사용
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + mon3)

        # 1년권 사용
        if i >= 12:
            dp[i] = min(dp[i], dp[i - 12] + year)


    print(f"#{t} {dp[12]}")

