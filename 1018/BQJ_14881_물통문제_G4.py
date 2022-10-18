import sys
from math import gcd

input = lambda :sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())
    if c > a and c > b:
        print("NO")
        exit()
    x = gcd(a, b)
    print(x)
    if c % x == 0:
        print('YES')
    else:
        print('NO')