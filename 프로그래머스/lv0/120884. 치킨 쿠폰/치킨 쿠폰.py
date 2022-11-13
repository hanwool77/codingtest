def solution(chicken):
    answer = 0
    while chicken >= 10:
        di, mo = divmod(chicken, 10)
        answer += di
        chicken = di + mo
    
    return answer