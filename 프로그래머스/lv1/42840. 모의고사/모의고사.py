def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3
    
    for i, answer in enumerate(answers):
        if one[i % 5] == answer:
            score[0] += 1
        if two[i % 8] == answer:
            score[1] += 1
        if three[i % 10] == answer:
            score[2] += 1
    
    answer = []
    for i, s in enumerate(score):
        if score[i] == max(score):
            answer.append((i + 1))
    return answer
    