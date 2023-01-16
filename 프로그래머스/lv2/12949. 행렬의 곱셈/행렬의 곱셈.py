def solution(arr1, arr2):
    N = len(arr1)
    M = len(arr2[0])
    answer = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            
    return answer

# 2 3 2   5 4 3   
# 4 2 4   2 4 1
# 3 1 4   3 1 1

# 1 4     3 3
# 3 2     3 3
# 4 1
