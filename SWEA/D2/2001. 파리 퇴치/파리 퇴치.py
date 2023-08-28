T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    ans = 0
    for i in range(N -  M + 1):
        for j in range(N  - M + 1):
            s = 0
            for x in range(M):
               for y in range(M):
                 s += arr[i + x][j + y]
            if s > ans:
                ans = s


    print(f'#{t + 1} {ans}')