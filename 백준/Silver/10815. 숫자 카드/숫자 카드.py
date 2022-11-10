import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
sang_card = list(map(int, input().split()))

M = int(input())
card = list(map(int, input().split()))

sang_card.sort()

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if sang_card[mid] == target:
            return 1
        elif sang_card[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in range(M):
    ans = binary_search(card[i], 0, N - 1)
    print(ans, end = ' ')
