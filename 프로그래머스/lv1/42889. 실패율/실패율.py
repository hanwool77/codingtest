def solution(N, stages):
    answer = []
    c = len(stages) # 사람 수
    for i in range(1, N + 1):
        fail = 0 if stages.count(i) == 0 else stages.count(i) / c
        c -= stages.count(i)
        if fail == 0:
            answer.append((i, 0))
        else:
            answer.append((i, fail))

    answer.sort(key = lambda x : x[1], reverse = True)
    return [i[0] for i in answer]