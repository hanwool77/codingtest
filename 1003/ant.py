def ant(number):
    num = number[0]
    count = 0
    next_ant = []

    for n in number:
        if n == num:
            count += 1
        else:
            next_ant.append(num)
            next_ant.append(count)
            num = n
            count = 1

    next_ant.append(num)
    next_ant.append(count)
    return next_ant


data = [1]
for i in range(20):
    data = list(map(str, data))
    print("".join(data))
    data = ant(data)