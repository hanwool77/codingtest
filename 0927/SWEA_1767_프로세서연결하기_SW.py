import sys
input = lambda :sys.stdin.readline().rstrip()

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(idx, cnt, plen): # idx: 확인한 코어 수, cnt: 전선을 연결한 코어 수, len: 코어 연결 시 전선 길이
    global maxCore
    global minLen

    if cnt + len(core) - idx < maxCore:
        return

    if idx == len(core):    # 코어 다 확인했을 경우
        if cnt > maxCore:   # 전선을 연결한 코어 수가 더 많을 경우
            maxCore = cnt
            minLen = plen
        elif cnt == maxCore:
            if plen < minLen:
                minLen = plen
        return

    x = core[idx][0]
    y = core[idx][1]

    for i in range(4):
        nx = x
        ny = y
        count = 0
        mx = x
        my = y

        while(True):
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                break
            if graph[nx][ny] == 1:
                count = 0
                break
            count += 1

        for j in range(count):
            mx += dx[i]
            my += dy[i]
            graph[mx][my] = 1

        if count == 0:
            dfs(idx + 1, cnt, plen)  # 코어 연결 X
        else:
            dfs(idx + 1, cnt + 1, plen + count)  # 코어 연결 O

        for j in range(count):
            graph[mx][my] = 0
            mx -= dx[i]
            my -= dy[i]

for t in range(1, T + 1):
    minLen = sys.maxsize
    maxCore = -sys.maxsize

    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    core = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and i != 0 and i != N-1 and j != 0 and j != N - 1:
                core.append((i, j))

    dfs(0, 0, 0)

    print(f"#{t} {minLen}")

