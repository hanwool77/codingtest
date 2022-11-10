T = int(input())

dx = [0, -1, 1, 0, 0] # 상, 하, 좌, 우
dy = [0, 0, 0, -1, 1]

# 반대
op = [0, 2, 1, 4, 3]    # 상, 하, 좌, 우

for t in range(1, T + 1):
    ans = 0
    n, m, k = map(int, input().split())
    arr = []
    for _ in range(k):
        x, y, c, d = map(int, input().split())
        arr.append((x, y, c, d))

    for _ in range(m):
        L = len(arr)

        for _ in range(L):  # 이동
            x, y, c, d = arr.pop(0)
            nx = x + dx[d]
            ny = y + dy[d]

            if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1:
                c //= 2
                d = op[d]
            arr.append([nx, ny, c, d])

        # 이동 후 좌표 겹치면 합치기
        arr.sort(key=lambda x: (x[0],x[1],-x[2]))

        i = 1
        while i < len(arr):
            if arr[i-1][0] == arr[i][0] and arr[i-1][1] == arr[i][1]:
                arr[i-1][2] += arr[i][2]
                arr.pop(i)
            else:
                i += 1
    for x, y, c, d in arr:
        ans += c

    print(f"#{t} {ans}")