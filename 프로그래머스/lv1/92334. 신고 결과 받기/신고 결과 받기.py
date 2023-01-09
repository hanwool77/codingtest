from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))
    user = defaultdict(set) # user[x]: x가 신고한 사람
    cnt = defaultdict(int)  # cnt[x]: x가 신고받은 수
    
    for r in report:
        a, b = r.split(" ") # a -> b에게 신고
        user[a].add(b)
        cnt[b] += 1
        
    for i, id in enumerate(id_list):
        for u in user[id]:
            if cnt[u] >= k:
                answer[i] += 1
            
    
    return answer