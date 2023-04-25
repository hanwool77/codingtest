import sys
input = lambda :sys.stdin.readline().rstrip()

N, K = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

country = sorted(country, key= lambda x : (-x[1], -x[2], -x[3]))
idx = [country[i][0] for i in range(N)].index(K)
ans = 0
for c in country:
    if c[0] == K:
        break
    else:
        if c[1:] != country[idx][1:]:
            ans += 1

print(ans + 1)