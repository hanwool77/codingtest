import math

def solution(number, limit, power):
    
    def get(number):
        cnt = 0
        for i in range(1, int(math.sqrt(number)) + 1):
            if number % i == 0:
                cnt += 1
                if i ** 2 != number:
                    cnt += 1
        return cnt
    array = [i for i in range(1, number + 1)]
    arr = []
    for a in array:
        arr.append(get(a))
    answer = 0
    for a in arr:
        answer += a if a <= limit else power
    return answer
   