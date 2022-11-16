def solution(lottos, win_nums):
    answer = [6, 6, 5, 4, 3, 2, 1]  # 당첨 내용
    
    맞은개수 = 0
    낙서 = lottos.count(0)
    for num in win_nums:
        if num in lottos:
            맞은개수 += 1
    
    return answer[맞은개수 + 낙서], answer[맞은개수]