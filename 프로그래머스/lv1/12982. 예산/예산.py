def solution(d, budget):
    answer = 0
    d.sort()
    for x in d:
        if x <= budget:
            answer += 1
            budget -= x
        else:
            break
    return answer