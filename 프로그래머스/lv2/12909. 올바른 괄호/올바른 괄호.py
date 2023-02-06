def solution(s):
    answer = True
    
    stack = []
    
    for x in s:
        if x == '(':
            stack.append(x)
        else:   # ')' 일경우
            if not stack:
                return False
            elif stack[-1] == ')':
                return False
            else:
                stack.pop()
    if stack:
        return False

    return True