from collections import deque

def solution(queue1, queue2):
    answer = 0
    n = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    
    for _ in range(n * 3 + 1):
        if s1 == s2:
            return answer
        elif s1 < s2:
            s1 += queue2[0]
            s2 -= queue2[0]
            queue1.append(queue2.popleft())
            answer += 1
        else:
            s2 += queue1[0]
            s1 -= queue1[0]
            queue2.append(queue1.popleft())
            answer += 1
    
    return -1