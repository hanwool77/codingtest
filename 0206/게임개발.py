import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
cx, cy, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
check[cx][cy] = 1

ans = 1
turn_time = 0

def turn_left(d):
    return (d - 1) % 4

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]

while True:
    d = turn_left(d)
    nx = cx + dx[d]
    ny = cy + dy[d]

    if 0 <= nx < n and 0 <= ny < m:
        if check[nx][ny] == 0 and graph[nx][ny] == 0:   # 한번도 가지 못했고, 육지일경우
            turn_time = 0
            cx = nx
            cy = ny
            check[nx][ny] = 1
            ans += 1
            continue
        else:
            turn_time += 1

        if turn_time == 4:  # 동,서,남,북 다 돌았을 경우
            nx = cx - dx[d]
            ny = cy - dy[d]

            if graph[nx][ny] == 0:
                break
            else:
                cx = nx
                cy = ny
                turn_time = 0

print(ans)
