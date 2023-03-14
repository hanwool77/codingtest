import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
print("SK" if N % 2 != 0 else "CY")