import sys
input = lambda :sys.stdin.readline().rstrip()

n, k = map(int, input().split())
d = [0] * (k + 1)   # d[k]: k원을 만들 수 있는 경우의 수
d[0] = 1

coin = []
for _ in range(n):
    coin.append(int(input()))

for c in coin:
    for i in range(c, k + 1):
        d[i] += d[i - c]

print(d[k])