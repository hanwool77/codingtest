from collections import deque

def solution(n, m, section):
    answer = 0
    section = deque(section)
    
    while section:
        s = section.popleft()
        
        while section and s + m - 1 >= section[0]:
            section.popleft()
        answer += 1
    
    return answer