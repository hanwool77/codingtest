import sys
input = lambda :sys.stdin.readline().rstrip()

s = input()
answer = []

for i in range(1, len(s) - 1):
    for j in range(i + 1, len(s)):
        first = s[:i]
        second = s[i:j]
        third = s[j:]
        answer.append(first[::-1] + second[::-1] + third[::-1])

answer.sort()
print(answer[0])

