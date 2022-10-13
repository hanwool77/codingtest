import sys
import heapq

input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapq.heapify(arr)

for _ in range(m):
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    heapq.heappush(arr, x + y)
    heapq.heappush(arr, x + y)

print(sum(arr))
