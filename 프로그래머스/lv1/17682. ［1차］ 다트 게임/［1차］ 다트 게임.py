import re

def solution(dartResult):
    패턴 = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
    answer = []
    
    for num, score, price in 패턴.findall(dartResult):
        num = int(num)
        if score == 'S':
            answer.append(num)
        elif score == 'D':
            answer.append(num ** 2)
        elif score == 'T':
            answer.append(num ** 3)
            
        if price == '*':
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
        
        elif price == '#':
            answer[-1] *= -1
          
    
    return sum(answer)