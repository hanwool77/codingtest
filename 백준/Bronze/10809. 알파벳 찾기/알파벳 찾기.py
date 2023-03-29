import sys
input = lambda :sys.stdin.readline().rstrip()

S = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for alpha in alphabet:
    print(S.find(alpha), end = ' ')

