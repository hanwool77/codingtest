import sys

'''
0개 부터 K개의 초밥 + 쿠폰을 적용한 후의 초밥 종류를 센 후
뒤에서 초밥 하나를 빼고 앞에 초밥하나를 추가했을 시 초밥의 종류를 count
'''


input = lambda : sys.stdin.readline().rstrip()

n, d, k, c = map(int, input().split())  # n: 접시 수, d: 초밥의 가짓 수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호
chobab = [int(input()) for _ in range(n)]   # 회전 초밥
chobab_kind = [0] * (d + 1) # 초밥의 종류

kind, res = 0, 0    # kind: 초밥의 종류, res: 초밥 종류의 최댓값

for i in range(k):  # 0개부터 k개의 초밥
    if chobab_kind[chobab[i]] == 0:
        kind += 1   # 처음 먹는 초밥일 경우 초밥의 종류 1 증가
    chobab_kind[chobab[i]] += 1 # i번째 초밥을 먹으면 chobab_kind 값 1 증가

# 쿠폰 적용
if chobab_kind[c] == 0:
    kind += 1
chobab_kind[c] += 1

res = kind

# 1부터 n까지 돌면서 앞에 초밥 빼고 뒤에 초밥 더해주기
for i in range(1, n):
    # 앞에 초밥 뺴기
    chobab_kind[chobab[i - 1]] -= 1
    if chobab_kind[chobab[i - 1]] == 0:
        kind -= 1

    # 뒤에 초밥 더하기
    if chobab_kind[chobab[(i - 1 + k) % n]] == 0:
        kind += 1
    chobab_kind[chobab[(i - 1 + k) % n]] += 1

    res = max(res, kind)

print(res)


