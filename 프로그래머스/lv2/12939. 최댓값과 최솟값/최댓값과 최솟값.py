def solution(s):
    answer = ''
    arr = s.split(" ")
    arr = list(map(int, arr))
    arr = sorted(arr)
    answer = str(arr[0]) + " " + str(arr[-1])
    return answer