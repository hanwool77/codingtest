def solution(x):
    d = 0
    for n in str(x):
        d += int(n)
        
    return True if x % d == 0 else False