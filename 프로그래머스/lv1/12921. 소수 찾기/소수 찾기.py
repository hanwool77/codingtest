from math import sqrt

def solution(n):
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False
    
    for i in range(2, int(sqrt(n)) + 1):
        if arr[i]:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1
    
    return arr.count(True)