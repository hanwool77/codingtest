from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

def solution(denum1, num1, denum2, num2):
    분모 = lcm(num1, num2)
    분자 = denum1 * (분모 // num1) + denum2 * (분모 // num2)
    약수 = gcd(분모, 분자)
    return 분자 // 약수, 분모 // 약수