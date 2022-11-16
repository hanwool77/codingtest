def solution(X, Y):
    answer = []
    
    for i in range(10):
        k = min(X.count(str(i)), Y.count(str(i)))
        for _ in range(k):
            answer.append(str(i))
            
    if not answer:
        return "-1"
    answer.sort(reverse = True)
    if answer[0] == '0':
        return '0'
    return "".join(answer)
        