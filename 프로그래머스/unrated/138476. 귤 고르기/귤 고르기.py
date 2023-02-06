from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    c = Counter(tangerine)
    c = sorted(list(c.items()), key = lambda x : x[1], reverse = True)
    
    for 크기, 개수 in c:
        k -= 개수
        answer += 1
        
        if k <= 0:
            break
    
    return answer