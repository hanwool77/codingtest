def solution(s):
    answer = 0
    x = s[0]
    x_cnt = 0
    not_x_cnt = 0
    i = 0
    while True:
        if i == len(s) - 1:
            answer += 1
            break
        if x == s[i]:
            x_cnt += 1
        else:
            not_x_cnt += 1
            
        if x_cnt == not_x_cnt:
            answer += 1
            x = s[i + 1]
            x_cnt = 0
            not_x_cnt = 0

        i += 1
    return answer