import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
data = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)


def calculate(idx, value, plus, minus, mul, div):
    global min_value
    global max_value
    if idx == N:
        if min_value > value:
            min_value = value
        if max_value < value:
            max_value = value
        return

    if plus > 0:
        calculate(idx + 1, value + data[idx], plus - 1, minus, mul, div)
    if minus > 0:
        calculate(idx + 1, value - data[idx], plus, minus - 1, mul, div)
    if mul > 0:
        calculate(idx + 1, value * data[idx], plus, minus, mul - 1, div)
    if div > 0:
        calculate(idx + 1, int(value / data[idx]), plus, minus, mul, div - 1)

calculate(1, data[0], plus, minus, mul, div)
print(max_value)
print(min_value)
