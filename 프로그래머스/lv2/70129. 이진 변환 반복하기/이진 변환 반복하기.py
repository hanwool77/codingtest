def solution(s):
    answer = []
    changeCnt = 0
    zeroCut = 0
    
   
    while s != "1":
        tmp = len(s.replace("0", ""))
        zeroCut += (len(s) - tmp)
        s = bin(tmp)[2:]
        changeCnt += 1

        
    return (changeCnt, zeroCut)