import heapq
import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())    # 연산의 개수
array = []
heapq.heapify(array)
for _ in range(N):
    x = int(input())
    if x == 0:  # 출력
        if len(array) == 0:
            print(0)
        else:
            num = heapq.heappop(array)
            print(num)
    else:
        heapq.heappush(array, x)

