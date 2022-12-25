import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
array = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)  # dp[i] = i번째까지 최대로 포장한 박스의 개수

for i in range(1, n + 1):
    dp[i] = 1
    for j in range(1, i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))



