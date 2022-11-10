from itertools import combinations

def solution(number):
    ans = 0
    for data in combinations(number, 3):
        if sum(data) == 0:
            ans += 1
    return ans