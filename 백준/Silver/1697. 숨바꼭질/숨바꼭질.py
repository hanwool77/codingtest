from collections import deque

MAX = 10 ** 5
n, k = map(int, input().split())
distance = [0] * (MAX + 1)

def bfs():
	q = deque()
	q.append(n)

	while q:
		x = q.popleft()
		if x == k:
			print(distance[x])
			break
		
		for nx in (x - 1, x + 1, x * 2):
			if 0 <= nx <= MAX and distance[nx] == 0:
				distance[nx] = distance[x] + 1
				q.append((nx))


bfs()