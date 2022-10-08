def fuc(x):
    if x % 2 == 0:  # 짝수인 경우
        bx = list(bin(x))
        bx[-1] = '1'
        return int("".join(bx), 2)
    else:   # 홀수인경우
        bx = '0b0' + bin(x)[2:]
        idx = bx.rfind('0')
        bx = list(bx)
        bx[idx] = '1'
        bx[idx + 1] = '0'
        return int("".join(bx), 2)

def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(fuc(n))
    return answer