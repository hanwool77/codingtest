def solution(arr):
    answer = list()
    answer.append(arr[0])

    for a in arr:
        if answer[-1] != a:
            answer.append(a)
        else:
            continue
    return answer