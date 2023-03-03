import sys
input = lambda :sys.stdin.readline().rstrip()

a, b = map(int, input().split())
arr = [0]

i = 1
n = 1

while i <= b:
    for _ in range(n):
        arr.append(n)
        i += 1
    n += 1

print(sum(arr[a:b + 1]))