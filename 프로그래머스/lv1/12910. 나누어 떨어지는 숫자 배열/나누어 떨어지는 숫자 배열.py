def solution(arr, divisor):
    answer = list()

    for a in arr:
        if a % divisor == 0:
            answer.append(a)

    return sorted(answer) if len(answer) > 0 else [-1]

