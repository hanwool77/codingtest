# 백준 9012

'''
괄호 주어졌을 때 올바른 괄호인지 확인
'''

from collections import deque

T = int(input())

for _ in range(T):
    ps = input()
    stack = deque()
    ans = "YES"

    for s in ps:
        if s == '(':
            stack.append(s)
        else:   # ')'일 경우
            if not stack:  # 비어있을 경우
                ans = "NO"
                break
            elif stack[-1] == '(':
                stack.pop()
            else:   # ')'일 경우
                ans = 'NO'
                break
    if stack:   # 스택이 남아있다면
        ans = 'NO'
    print(ans)
