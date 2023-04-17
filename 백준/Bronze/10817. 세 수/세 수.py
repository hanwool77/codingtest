import sys
input = lambda :sys.stdin.readline().rstrip()

data = list(map(int, input().split()))
data.sort()
print(data[1])
