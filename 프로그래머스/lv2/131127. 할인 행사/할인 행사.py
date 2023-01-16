from collections import Counter

def solution(want, number, discount):
    answer = 0
    check = {}
    
    for w, n in zip(want, number):
        check[w] = n
    
    answer = 0
    for i in range(len(discount) - 10 + 1):
        c = Counter(discount[i:i + 10])
        if c == check:
            answer += 1

     
    return answer