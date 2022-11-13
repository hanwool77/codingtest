def solution(dots):
    arr = set()

    for i in range(4):
        for j in range(i + 1, 4):
            cur = (dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0])
            if cur in arr:
                return 1
            arr.add(cur)
    
    return 0