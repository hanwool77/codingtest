def solution(n, lost, reserve):
    cloth = [0] + [1] * (n) + [0]
    for l in lost:
        cloth[l] -= 1
    for r in reserve:
        cloth[r] += 1
        
    for i in range(1, n + 1):
        if cloth[i] == 0 and cloth[i - 1] >= 2:
            cloth[i] += 1
            cloth[i - 1] -= 1
        if cloth[i] == 0 and cloth[i + 1] >= 2:
            cloth[i] += 1
            cloth[i + 1] -= 1
    answer = 0
    for i in range(1, n + 1):
        if cloth[i] >= 1:
            answer += 1
    return answer
    