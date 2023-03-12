import sys
input = lambda :sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    to_bin = bin(N)[2:][::-1]
    for i, b in enumerate(to_bin):
        if b == '1':
            print(i, end = ' ')
    print()