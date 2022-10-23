import sys
import heapq
from collections import deque

input = lambda :sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())    # 통나무 개수
    arr = list(map(int, input().split()))
    heapq.heapify(arr)

    통나무 = deque()
    통나무.append(heapq.heappop(arr))

    while arr:
        if arr:
            통나무.appendleft(heapq.heappop(arr))
        if arr:
            통나무.append(heapq.heappop(arr))

    ans = abs(통나무[0] - 통나무[-1])

    for i in range(len(통나무) - 1):
        diff = abs(통나무[i + 1] - 통나무[i])
        if diff > ans:
            ans = diff

    print(ans)