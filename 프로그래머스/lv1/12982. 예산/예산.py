def solution(d, budget):
    arr = sorted(d)
    ans = 0
    
    for a in arr:
        if budget - a >= 0:
            ans += 1
            budget -= a
    
    return ans
    