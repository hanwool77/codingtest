import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
array = list()
for _ in range(N):
    name, kor, eng, mat = input().split()
    array.append((name, int(kor), int(eng), int(mat)))

array.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(array[i][0])