from itertools import combinations
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

data = [i for i in range(n)]

team = list(combinations(data, n // 2))
result = int(1e9)

for i in range(len(team) // 2):
    teamS = team[i] # 스타트 팀
    teamL = team[len(team) - i - 1] # 링크 팀

    sum_s = 0   # 스타트 팀 능력치
    sum_l = 0   # 링크 팀 능력치

    for sx, sy in combinations(teamS, 2):
        sum_s += arr[sx][sy] + arr[sy][sx]

    for lx, ly in combinations(teamL, 2):
        sum_l += arr[lx][ly] + arr[ly][lx]

    if abs(sum_s - sum_l) < result:
        result = abs(sum_s - sum_l)

print(result)
