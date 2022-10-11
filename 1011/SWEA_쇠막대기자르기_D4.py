T = int(input())

for t in range(1, T + 1):
    data = input()
    ans = 0
    stick = 0

    for i in range(len(data)):
        if data[i] == '(':  # 막대기 일 경우
            stick += 1
        else:
            if data[i - 1] == '(':   # 레이저일 경우
                stick -= 1
                ans += stick
            else:   # 막대기 끝일 경우
                ans += 1
                stick -= 1

    print(f"#{t} {ans}")