import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
human = []

for _ in range(n):
    w, h = map(int, input().split())    # w: 몸무게, h: 키
    human.append((w, h))

ans = [0] * n

for i in range(n):
    cnt = 1 # 자신보다 덩치가 큰 사람의 수
    for j in range(n):
        if i == j:
            continue
        if human[i][0] < human[j][0] and human[i][1] < human[j][1]:
            cnt += 1
    ans[i] = cnt

print(*ans)

