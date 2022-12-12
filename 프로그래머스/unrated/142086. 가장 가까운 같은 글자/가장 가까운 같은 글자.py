def solution(s):
    answer = []
    d = dict()
    for idx, 문자 in enumerate(s):
        if 문자 in d: # 처음 나오지 않을 경우
            answer.append(idx - d[문자])
            d[문자] = idx
        else: # 처음 나올 경우
            answer.append(-1)
            d[문자] = idx
    return answer