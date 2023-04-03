import sys
input = lambda :sys.stdin.readline().rstrip()

N = input()
F = int(input())

for i in range(100):
    c = N[:len(N)-2] + str(i).zfill(2)
    if int(c) % F == 0:
        break

print(str(i).zfill(2))
