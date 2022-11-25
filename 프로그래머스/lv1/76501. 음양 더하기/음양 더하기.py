def solution(absolutes, signs):
    answer = 0
    
    for 숫자, 부호 in zip(absolutes, signs):
        if 부호 == True:
            answer += 숫자
        else:
            answer -= 숫자
    return answer