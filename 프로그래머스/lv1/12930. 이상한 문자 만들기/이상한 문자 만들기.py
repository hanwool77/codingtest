def solution(s):
    s = s.split(" ")
    answer = ''
    
    for a in s:
        for i, v in enumerate(a):
            if i % 2 == 0:
                answer += v.upper()
            else:
                answer += v.lower()
        answer += ' '
    
    return answer[:-1]