def solution(elements):
    answer = set()
    n = len(elements)
    for i in range(n):
        s = 0
        for j in range(n):
            s += elements[(i + j) % n]
            answer.add(s)
        
    return len(answer)