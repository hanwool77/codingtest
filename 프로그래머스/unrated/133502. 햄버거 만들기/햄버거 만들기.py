def solution(ingredient):
    ans = 0
    재료 = []
    
    for i in ingredient:
        재료.append(i)
        if 재료[-4:] == [1, 2, 3, 1]:
            ans += 1
            for _ in range(4):
                재료.pop()
    return ans
        
    