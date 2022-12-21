import sys
input = lambda :sys.stdin.readline().rstrip()

score = []
총점 = 0
for i in range(1, 9):
    s = int(input())
    score.append((s, i))

score.sort(key=lambda x:x[0], reverse=True)
참가자 = []

for i in range(5):
    참가자.append(score[i][1])
    총점 += score[i][0]

참가자.sort()

print(총점)
print(*참가자)
