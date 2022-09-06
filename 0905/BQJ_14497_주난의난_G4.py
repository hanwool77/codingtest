from collections import deque
import sys

input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())    # 1 <= n, m <= 300  교실: n x m
x1, y1, x2, y2 = map(int, input().split())  # 주난이의 위치 x1,y1  범인의 위치 x2,y2

graph = [list(input()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

