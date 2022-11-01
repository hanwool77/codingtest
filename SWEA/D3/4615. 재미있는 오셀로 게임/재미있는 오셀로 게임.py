T = int(input())

# 8방 탐색
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def count():
    black, white = 0, 0
    for i in range(N):
        for j in range(N):
            if array[i][j] == 1:
                black += 1
            elif array[i][j] == 2:
                white += 1
    return black, white

for t in range(1, T + 1):
    black, white = 0, 0
    N, M = map(int, input().split())
    array = [[0] * N for _ in range(N)]

    # 초기 돌 설정
    array[N // 2 - 1][N // 2 - 1] = 2
    array[N // 2][N // 2] = 2
    array[N // 2 - 1][N // 2] = 1
    array[N // 2][N // 2 - 1] = 1

    for _ in range(M):
        y, x, dol = map(int, input().split())
        y -= 1
        x -= 1
        array[x][y] = dol
        for i in range(8):
            nx, ny = x, y
            candidate = []
            while True:
                nx += dx[i]
                ny += dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    break
                if array[nx][ny] == 0:
                    break
                elif array[nx][ny] == array[x][y]:
                    for cx, cy in candidate:
                        array[cx][cy] = array[x][y]
                    break
                else: # 다를경우
                    candidate.append((nx, ny))
    black, white = count()

    print(f"#{t} {black} {white}")