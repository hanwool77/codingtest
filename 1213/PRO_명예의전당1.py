import heapq

def solution(k, score):
    answer = []
    q = []
    for s in score:
        if len(q) < k:
            heapq.heappush(q, s)
        else:
            if s > q[0]:
                heapq.heappop(q)
                heapq.heappush(q, s)
        answer.append(q[0])
    return answer