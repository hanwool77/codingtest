import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
ans = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            t = str(i) + str(j) + str(k)
            if t.count('3') >= 1:
                ans += 1

print(ans)