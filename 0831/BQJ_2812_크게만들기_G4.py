import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
number = list(map(int, input()))

stack = []
er = k

for i in range(n):
    while stack and er > 0:
        if stack[-1] < number[i]:
            stack.pop()
            er -= 1
        else:
            break

    stack.append(number[i])

print("".join(list(map(str, stack[:n-k]))))