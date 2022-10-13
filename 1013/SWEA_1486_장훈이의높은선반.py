T = int(input())


def DFS(n, ssum):
    global ans
    if n == N:
        if ssum > B and ans > ssum - B:
            ans = ssum - B
        return

    DFS(n + 1, ssum + lst[n])    # 포함하는 경우
    DFS(n + 1, ssum)    # 포함하지 않는 경우


for t in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 12345678
    DFS(0, 0)
    print(f'#{t} {ans}')

