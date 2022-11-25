def solution(numbers):
    집합 = set([i for i in range(10)])
    numbers = set(numbers)
    
    return sum(집합.difference(numbers))