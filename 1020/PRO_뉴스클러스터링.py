import re
from collections import Counter
p = re.compile(r'[a-z]{2}')

def solution(str1, str2):
    for i in range(len(str1) - 1):
        s1 = str1[i:i+2].lower()
        s2 = str2[i:i + 2].lower()
        first = list()
        second = list()
        if p.match(s1):
            first.append(s1)
        if p.match(s2):
            second.append(s2)

        교집합 = set(first) & set(second)
        합집합 = set(first) | set(second)

        a = Counter(first)
        b = Counter(second)
        x, y = 0, 0 # 최종 답안
        for i in 교집합:
            x += min(a[i], b[i])
        for i in 합집합:
            y += max(a[i], b[i])

        return int(x / y * 65536)

testcase = [["FRANCE", "french"]]
for t in testcase:
    solution(t[0], t[1])