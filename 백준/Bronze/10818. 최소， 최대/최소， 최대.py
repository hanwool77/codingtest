import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
data = list(map(int, input().split()))
print(min(data), end = ' ')
print(max(data), end = " ")