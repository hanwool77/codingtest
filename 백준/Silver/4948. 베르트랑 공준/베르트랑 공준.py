import math
import sys
input = lambda :sys.stdin.readline().rstrip()

def estre(n):
    length = 2 * n + 1
    array = [True] * length
    cnt = 0

    for i in range(2, int(math.sqrt(length)) + 1):
        j = 2
        if array[i]:
            while i * j <= length - 1:
                array[i * j] = False
                j += 1

    # for idx, a in enumerate(array):
    #     print(idx, a)
    for i in range(n + 1, length):
        if i >= 2 and array[i]:
            cnt += 1
    return cnt

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(estre(n))