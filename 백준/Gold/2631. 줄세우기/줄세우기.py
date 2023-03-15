import sys
input = lambda :sys.stdin.readline().rstrip()

''' 
아이들을 최소 횟수로 옮겨서 정렬을 만들려면 현재 아이들이 줄 서 있는 리스트에서 최장 길이 수열을 구한 후 
아이들의 수에서 최장 길이 수열의 최댓값을 빼주면 된다.

3 7 5 2 6 1 4
=> 3 5 6 이렇게 최장길이 수열이 있으므로 1, 2, 4, 7 아이들만 옮기면 가장 아이들을 적게 옮기고 정렬을 할 수 있음

'''

N = int(input())
children = [0] + [int(input()) for _ in range(N)]

dp = [1] * (N + 1)  # 최장 길이 수열

for i in range(1, N + 1):
    for j in range(1, i):
        if children[i] > children[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))