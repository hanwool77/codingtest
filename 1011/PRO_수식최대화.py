from itertools import permutations
from collections import deque


def make_result(expression, operation):
    array = deque()
    num = ''
    for ex in expression:
        if ex.isdigit():
            num += ex
        else:
            array.append(num)
            num = ''
            array.append(ex)
    array.append(num)

    for op in operation:
        stack = []
        while len(array) != 0:
            x = array.popleft()
            if x == op:
                stack.append(str(eval(stack.pop() + op + array.popleft())))
            else:
                stack.append(x)
        array = deque(stack)

    return abs(int(array[0]))


def solution(expression):
    answer = 0
    for operation in list(permutations(['+', '-', '*'], 3)):
        answer = max(answer, make_result(expression, operation))

    return answer