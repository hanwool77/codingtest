import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
tree_dict = defaultdict(int)
tree_cnt = 0

while True:
    tree = input()
    if not tree:
        break
    tree_dict[tree] += 1
    tree_cnt += 1

tree_dict = sorted(tree_dict.items(), key=lambda x: x[0])
for key, val in tree_dict:
    print('%s %.4f' %(key, val / tree_cnt * 100))
