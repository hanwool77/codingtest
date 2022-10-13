n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)

result = 0
for i in range(n):
    result = max(rope[i] * (i + 1), result)
    print(result)

print(result)
