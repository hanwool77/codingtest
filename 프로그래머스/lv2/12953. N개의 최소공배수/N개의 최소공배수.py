import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def solution(arr):
    answer = 1
    for i in range(len(arr)):
        answer = lcm(answer, arr[i])
    return answer