import sys
input = lambda :sys.stdin.readline().rstrip()

N, d, k, c = map(int, input().split())  # N: 회전 초밥 벨트에 놓인 접시 수 d: 초밥의 가지 수, k: 연속해서 먹는 접시 수 c: 쿠폰번호
chobab = [int(input()) for _ in range(N)]   # 회전 초밥 리스트
chobab_kind = [0] * (d + 1) # 초밥 종류 리스트

kind = res = 0

# 처음에 k개 초밥 먹기
for i in range(k):
    if chobab_kind[chobab[i]] == 0:
        kind += 1
    chobab_kind[chobab[i]] += 1

# 쿠폰 적용하기
if chobab_kind[c] == 0:
    kind += 1
chobab_kind[c] += 1

res = kind

# 회전초밥 1번부터 n까지 돌면서 앞에는 빼주고 뒤에는 더해주기
for i in range(1, N + 1):
    # 앞에 초밥 뺴주기
    chobab_kind[chobab[i - 1]] -= 1
    if chobab_kind[chobab[i - 1]] == 0:
        kind -= 1

    # 뒤에 초밥 더해주기
    if chobab_kind[chobab[(i + k - 1) % N]] == 0:
        kind += 1
    chobab_kind[chobab[(i + k - 1) % N]] += 1
    res = max(res, kind)

print(res)
