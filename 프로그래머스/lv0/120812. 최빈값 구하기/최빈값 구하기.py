def solution(array):
    answer = []
    
    집합 = set(array)
    if len(집합) == 1:
        return 집합.pop()
    
    for x in 집합:
        answer.append((x, array.count(x)))
    
    answer = sorted(answer, key = lambda x : x[1], reverse = True)
    
    return answer[0][0] if answer[0][1] > answer[1][1] else -1