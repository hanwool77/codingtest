def solution(n):
    cnt1 = bin(n)[2:].count("1")
    for i in range(n + 1, 1000001):
        cnt = bin(i)[2:].count("1")
        if cnt1 == cnt:
            return i
