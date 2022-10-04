import sys
input = lambda : sys.stdin.readline().rstrip()

graph = []
for i in range(19):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]

for x in range(19):
    for y in range(19):
        if graph[x][y]:
            r = graph[x][y]

            for i in range(4):
                count = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == r:
                    count += 1

                    if count == 5:  # 육목인지 아닌지 판단
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and graph[nx+dx[i]][ny + dy[i]] == r:  # 육목일 경우
                            break
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and graph[x - dx[i]][y - dy[i]] == r:  # 육목일 경우
                            break

                        print(r)
                        print(x + 1, y + 1)
                        sys.exit()

                    nx += dx[i]
                    ny += dy[i]

print(0)