T = int(input())
dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]

def dfs(x, y, visited, cnt, way):
    global i, j, ans
    if way >= 4:
        return
    # 종료 조건
    if x == i and y == j and way == 3:
        if cnt > ans:
            ans = cnt
            return

    # 직진인 경우
    nx = x + dx[way]
    ny = y + dy[way]
    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] not in visited:
        dfs(nx, ny, visited + [graph[nx][ny]], cnt + 1, way)
    # 회전할 경우
    if way + 1 <= 3:
        nx = x + dx[way + 1]
        ny = y + dy[way + 1]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] not in visited:
            dfs(nx, ny, visited + [graph[nx][ny]], cnt + 1, way + 1)


for t in range(1, T + 1):
    ans = -1
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            dfs(i, j, [graph[i][j]], 1, 0)

    print(f'#{t} {ans}')

