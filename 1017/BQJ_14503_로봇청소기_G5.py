import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def turn_left():
    global d
    d = (d - 1) % 4

x, y = r, c
graph[x][y] = 2  # 현재위치 청소
count = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]  # 북0 동1 남2 서3

while True:
    check = False

    for _ in range(4):  # 네방향 탐색
        turn_left()
        nx = x + dx[d]
        ny = y + dy[d]  # 왼쪽 방향으로 갈 곳

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:  # 왼쪽 방향에 아직 청소하지 않은 곳이 있으면
            count += 1  # 청소
            graph[nx][ny] = 2   # 청소하기
            x, y = nx, ny
            check = True    # 청소 했다고 check
            break

    if not check:   # 네 방향 모두 청소가 이미 되어있거나 벽이라면
        nx = x - dx[d]
        ny = y - dy[d]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 2:
            x = nx
            y = ny
        else:
            print(count)
            break

