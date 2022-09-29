import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
data = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

minRes = float('inf')
maxRes = float('-inf')

def dfs(res, idx, plus, minus, mul, div):
    global minRes
    global maxRes
    if idx == len(data):
        minRes = min(minRes, res)
        maxRes = max(maxRes, res)
        return

    if plus > 0:
        dfs(res + data[idx], idx + 1, plus - 1, minus, mul, div)
    if minus > 0:
        dfs(res - data[idx], idx + 1, plus, minus - 1, mul, div)
    if mul > 0:
        dfs(res * data[idx], idx + 1, plus, minus, mul - 1, div)
    if div > 0:
        dfs(int(res / data[idx]), idx + 1, plus, minus, mul, div - 1)

dfs(data[0], 1, plus, minus, mul, div)
print(maxRes)
print(minRes)


