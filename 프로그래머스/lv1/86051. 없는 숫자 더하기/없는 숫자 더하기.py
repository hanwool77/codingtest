def solution(numbers):
    answer = 0
    
    for i in range(1, 10):
        if numbers.count(i) == 0:
            answer += i
            
    return answer




# def solution(numbers):
#     집합 = set([i for i in range(10)])
#     numbers = set(numbers)
    
#     return sum(집합.difference(numbers))