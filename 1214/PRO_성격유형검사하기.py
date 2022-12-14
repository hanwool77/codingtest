from collections import defaultdict

def solution(survey, choices):
    answer = ''
    d = defaultdict(int)
    for i, c in enumerate(choices):
        if c <= 4:  # 앞
            d[survey[i][0]] += abs(4 - c)
        else: #뒤
            d[survey[i][1]] += abs(4 - c)
    answer += 'R' if d['R'] >= d['T'] else 'T'
    answer += 'C' if d['C'] >= d['F'] else 'F'
    answer += 'J' if d['J'] >= d['M'] else 'M'
    answer += 'A' if d['A'] >= d['N'] else 'N'
    return answer