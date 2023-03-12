import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
data = [int(input()) for _ in range(N)]

data = sorted(data)

for d in data:
    print(d)