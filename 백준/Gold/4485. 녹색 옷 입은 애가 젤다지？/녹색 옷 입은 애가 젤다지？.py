import sys
import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(1e9)
t = 0

while True:
    N = int(input())    # 동굴의 크기
    t += 1
    if N == 0:
        sys.exit()

    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (0, 0, 0))

    while q:
        dist, cx, cy = heapq.heappop(q)
        if distance[cx][cy] < dist:
            continue

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    ans = distance[N - 1][N - 1] + graph[0][0]
    print(f'Problem {t}: {ans}')


