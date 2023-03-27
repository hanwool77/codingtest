import sys

N = int(input())

for i in range(N):
    star = i + 1
    space = N - i - 1

    for k in range(space):
        print(' ', end = '')
    for k in range(star):
        print('*', end = ' ')
    print()