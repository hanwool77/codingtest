def solution(s):
    answer = ''
    arr = s.split(" ")
    for strings in arr:
        for i, s in enumerate(strings):
            if i % 2 == 0:
                answer += s.upper()
            else:
                answer += s.lower()
        answer += ' '
        
    return answer[:-1]