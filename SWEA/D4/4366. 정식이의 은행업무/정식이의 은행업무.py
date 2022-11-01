T = int(input())

def convertTo3(n):
    data = ''
    while n > 0:
        n, div = divmod(n, 3)
        data += str(div)
    return data[::-1]

for t in range(1, T + 1):
    two = list(input())
    three = input()
    ans = 0

    for i in range(len(two)):
        if two[i] == '0':
            two[i] = '1'
        else:
            two[i] = '0'
        x = int('0b' + "".join(two), 2) # x => 10진수 숫자
        convert3 = convertTo3(x)
        if two[i] == '0':
            two[i] = '1'
        else:
            two[i] = '0'
        if len(convert3) != len(three):
            continue
        cnt = 0
        for j in range(len(three)):
            if convert3[j] != three[j]:
                cnt += 1
        if cnt == 1:
            ans = x
            break
    print(f"#{t} {ans}")

