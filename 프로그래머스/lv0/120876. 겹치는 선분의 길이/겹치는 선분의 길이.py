from collections import defaultdict

def solution(lines):
    선분 = defaultdict(int)
    answer = 0
    for line in lines:
        s = min(line)
        e = max(line)
        for i in range(s, e):
            선분[i] += 1
    for 선 in 선분:
        if 선분[선] >= 2:
            answer += 1
    return answer