from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(dict(answer))[0]