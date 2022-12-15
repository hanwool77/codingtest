import sys

input = lambda: sys.stdin.readline().rstrip()

k = int(input())
inorder = list(map(int, input().split()))


def dfs(inorder, depth):
    mid = len(inorder) // 2

    answer[depth].append(inorder[mid])
    if len(inorder) == 1:
        return
    dfs(inorder[:mid], depth + 1)
    dfs(inorder[mid + 1:], depth + 1)


answer = [[] for _ in range(k)]
dfs(inorder, 0)
for a in answer:
    print(*a)
