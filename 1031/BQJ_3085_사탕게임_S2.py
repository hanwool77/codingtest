import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())    # 3 <= N <= 50
candy = []
for _ in range(N):
    candy.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def count_candy():
    # 행
    max_row_cnt = 0
    max_col_cnt = 0
    for i in range(N):
        row_cnt = 1
        for j in range(1, N):
            if candy[i][j] == candy[i][j - 1]:
                   row_cnt += 1
            else:
                max_row_cnt = max(max_row_cnt, row_cnt)
                row_cnt = 1
        max_row_cnt = max(max_row_cnt, row_cnt)

    # 열
    for j in range(N):
        col_cnt = 1
        for i in range(1, N):
            if candy[i][j] == candy[i - 1][j]:
                col_cnt += 1
            else:
                max_col_cnt = max(max_col_cnt, col_cnt)
                col_cnt = 1
        max_col_cnt = max(max_col_cnt, col_cnt)
    return max(max_row_cnt, max_col_cnt)

ans = 0
for x in range(N):
    for y in range(N):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if candy[x][y] != candy[nx][ny]:    # 인접한 곳과 사탕 색이 다르면
                    # 교환
                    candy[x][y], candy[nx][ny] = candy[nx][ny], candy[x][y]
                    ans = max(ans, count_candy())
                    # 다시 원위치
                    candy[x][y], candy[nx][ny] = candy[nx][ny], candy[x][y]

print(ans)