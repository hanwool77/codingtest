def solution(a, b, n):
    answer = 0
    while True:
        x, y = divmod(n, a)
        if x == 0:
            break
        answer += x * b
        n = x * b + y
    return answer