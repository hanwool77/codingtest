def solution(s):
    answer = ''
    s = s.split(" ")
    
    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()
            
    return " ".join(s)