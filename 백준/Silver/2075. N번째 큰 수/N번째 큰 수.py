import sys
import heapq
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
q = []
for _ in range(n):
    data = list(map(int, input().split()))
    for d in data:
        if len(q) < n:
            heapq.heappush(q, d)
        else:
            if q[0] < d:
                heapq.heappop(q)
                heapq.heappush(q, d)

print(q[0])