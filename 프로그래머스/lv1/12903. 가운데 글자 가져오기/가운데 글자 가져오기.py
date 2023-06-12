def solution(s):
    n = len(s) // 2
    
    return s[n] if len(s) % 2 != 0 else s[n-1:n + 1]