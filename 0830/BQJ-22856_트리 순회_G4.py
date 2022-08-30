import sys

sys.setrecursionlimit(10 ** 9)

class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def inorder(node):  # 중위 순회
    if node.left != -1:
        inorder(tree[node.left])
    inorder_list.append(node.item)
    if node.right != -1:
        inorder(tree[node.right])

def similar_inorder(node):   # 유사 중위 순회
    visited[node.item] = True
    global cnt
    if node.left != -1 and not visited[node.left]:
        cnt += 1
        similar_inorder(tree[node.left])
    if node.right != -1 and not visited[node.right]:
        cnt += 1
        similar_inorder(tree[node.right])
    if node.item == inorder_list[-1]:
        print(cnt)
        exit()
    if node.item != 1:
        cnt += 1
        similar_inorder(tree[parent[node.item]])

n = int(input())    # 노드의 개수 1 <= n <= 100,000
tree = {}   # 트리
parent = [0] * (n + 1)  # 부모를 저장하는 리스트
visited = [False] * (n + 1)

for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a] = Node(a, b, c)
    if b != -1:
        parent[b] = a
    if c != -1:
        parent[c] = a

inorder_list = []
inorder(tree[1])    # 중위 순회
cnt = 0
similar_inorder(tree[1])    # 유사 중위 순회
