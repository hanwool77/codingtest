import sys
input = lambda :sys.stdin.readline().rstrip()

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if a == b == c:
        print("Equilateral")
        continue
    elif a + b <= c or b + c <= a or a + c <= b:
        print('Invalid')
    elif a == b or b == c or c == a:
        print("Isosceles")
    else: print("Scalene")
