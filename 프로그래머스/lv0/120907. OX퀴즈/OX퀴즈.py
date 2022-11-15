def solution(quiz):
    answer = []
    
    for q in quiz:
        식 = q.split(" ")
        if 식[1] == '+':
            if int(식[0]) + int(식[2]) == int(식[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif 식[1] == '-':
            if int(식[0]) - int(식[2]) == int(식[4]):
                answer.append("O")
            else:
                answer.append("X")
                
    return answer
    