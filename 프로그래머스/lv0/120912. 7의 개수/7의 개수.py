def solution(array):
    answer = 0
    array = map(str, array)
    for a in array:
        answer += a.count('7')
    return answer