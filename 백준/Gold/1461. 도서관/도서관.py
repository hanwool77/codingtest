import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int,input().split())
book = list(map(int,input().split()))
pos = [b for b in book if b > 0]
neg = [-b for b in book if b < 0]

pos.sort(reverse=True)
neg.sort(reverse=True)

distance = []
result = 0
max_distance = 0

for i in range(0, len(pos), m):
    distance.append(pos[i] * 2)
    max_distance = max(max_distance, pos[i])

for i in range(0, len(neg), m):
    distance.append(neg[i] * 2)
    max_distance = max(max_distance, neg[i])

print(sum(distance) - max_distance)
