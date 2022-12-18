from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)

    numbers.rotate(-1) if direction == "left" else numbers.rotate(1)
    answer = list(numbers)
    return answer