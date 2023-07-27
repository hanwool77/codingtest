from math import sqrt
from itertools import combinations

def solution(nums):

    ans = 0
    def is_prime_number(num):
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    for data in combinations(nums, 3):
        if is_prime_number(sum(data)):
            ans += 1
    
    return ans