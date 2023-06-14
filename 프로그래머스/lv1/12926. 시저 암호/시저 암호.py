def solution(s, n):
    small = 'abcdefghijklmnopqrstuvwxyz'
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    
    for a in s:
        if a.isalpha():
            if a.islower():
                answer += small[(small.index(a) + n) % 26]
            else:
                answer += big[(big.index(a) + n) % 26]
        else:
            answer += a
            
    return answer