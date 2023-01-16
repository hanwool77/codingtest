import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
plans = input().split()

dir = {
    'L':(0, -1),
    'R':(0, 1),
    'U':(-1, 0),
    'D':(1, 0)
}

sx, sy = (1, 1)

for plan in plans:
    nx = sx + dir[plan][0]
    ny = sy + dir[plan][1]

    # 이동할 곳이 범위 밖이면 무시
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    # 이동할 곳이 범위 안이면 이동
    sx, sy = nx, ny

print(sx, sy)