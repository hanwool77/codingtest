import sys
from bisect import bisect_left

input = lambda :sys.stdin.readline().rstrip()

P = int(input())

for _ in range(P):   # 테스트 케이스만큼 반복
    t = list(map(int, input().split()))
    student = t[1:]
    ans = 0
    line = []

    for s in student:
        x = bisect_left(line, s)
        ans += len(line) - x
        line.insert(x, s)

    print(t[0], end = ' ')
    print(ans)
