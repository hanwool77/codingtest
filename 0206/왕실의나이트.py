import sys
input = lambda :sys.stdin.readline().rstrip()

dx = [-1, -2 ,-2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

s = input()
ans = 0

x = int(s[1]) - 1
y = ord(s[0]) - 97

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < 8 and 0 <= ny < 8:
        ans += 1

print(ans)
