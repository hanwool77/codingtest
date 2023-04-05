import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = lambda :sys.stdin.readline().rstrip()

T = int(input())


def dfs(x, arr):
    global visited, result
    visited[x] = True
    arr.append(x)
    nx = data[x]

    if visited[nx]:
        if nx in arr:
            result += len(arr[arr.index(nx):])
    else:
        dfs(nx, arr)


for _ in range(T):
    n = int(input())    # 학생들의 수
    data = [0] + list(map(int, input().split()))

    result = 0
    visited = [False] * (n + 1)


    for i in range(1, n + 1):
        arr = []
        if not visited[i]:
            dfs(i,  arr)
    print(n - result)