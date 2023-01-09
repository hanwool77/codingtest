import sys

input = lambda :sys.stdin.readline().rstrip()


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for a in array:
    answer = max(answer, min(a))

print(answer)