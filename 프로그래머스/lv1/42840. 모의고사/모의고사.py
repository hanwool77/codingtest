def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    arr = [0, 0, 0]
    
    for i, a in enumerate(answers):
        if one[i % len(one)] == a:
            arr[0] += 1
        if two[i % len(two)] == a:
            arr[1] += 1
        if three[i % len(three)] == a:
            arr[2] += 1
    
    answer = []
    for i, a in enumerate(arr, start = 1):
        if a == max(arr):
            answer.append(i)
    
    return answer