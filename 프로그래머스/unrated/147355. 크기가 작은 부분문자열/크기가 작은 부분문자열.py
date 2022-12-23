from itertools import combinations

def solution(t, p):
    answer = 0
    i = 0
    while i <= len(t) - len(p):
        부분문자열 = t[i:i + len(p)]
        if int(부분문자열) <= int(p):
            answer += 1
        i += 1
    return answer