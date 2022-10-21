T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(n, x, y, num):
    if n == 6:
        sset.add(num)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 4 and 0 <= ny < 4:
            DFS(n + 1, nx, ny, num * 10 + arr[nx][ny])

for t in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    sset = set()
    for i in range(4):
        for j in range(4):
            DFS(0, i, j, arr[i][j])

    print(f'#{t} {len(sset)}')
