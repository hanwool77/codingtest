def solution(k, m, score):
    ans = 0
    score.sort(reverse = True)
    i = m - 1
    while i < len(score):
        ans += m * score[i]
        i += m
    return ans