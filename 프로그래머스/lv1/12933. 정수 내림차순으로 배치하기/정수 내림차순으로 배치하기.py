def solution(n):
    x = list(str(n))
    x = sorted(x, reverse = True)
    return int("".join(x))