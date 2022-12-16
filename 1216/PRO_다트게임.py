def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'A')
    for i in dartResult:
        if i.isdigit() or i == 'A':
            answer.append(10 if i == 'A' else int(i))
        elif i == 'S':
            pass
        elif i == 'D':
            answer[-1] = answer[-1] ** 2
        elif i == 'T':
            answer[-1] = answer[-1] ** 3
        elif i == '#':  # 아차상
            answer[-1] *= -1
        elif i == '*':   # 스타상
            if len(answer) > 1:
                answer[-1] *= 2
                answer[-2] *= 2
            else:
                answer[-1] *= 2
    return sum(answer)

dartResult = ['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']

for d in dartResult:
    print(solution(d))