import sys
from collections import defaultdict
input = lambda :sys.stdin.readline().rstrip()

dict = defaultdict(int)

word = input()

if len(word) == 1:
    print(word.upper())
    sys.exit()

for w in word:
    w = w.upper()
    dict[w] += 1

dict = sorted(dict.items(), key=lambda x : x[1], reverse=True)

print("?" if dict[0][1] == dict[1][1] else dict[0][0])
