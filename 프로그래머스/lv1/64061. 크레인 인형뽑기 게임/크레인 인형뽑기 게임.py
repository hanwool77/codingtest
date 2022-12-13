from collections import deque

def solution(board, moves):
    answer = 0
    stack = deque()
    
    n = len(board)
    for m in moves:
        c = 0
        for i in range(n):
            if board[i][m - 1] > 0:
                c = 1
                break
        if c == 0:
            continue
        x = board[i][m - 1]
        board[i][m - 1] = 0
        
        if stack and stack[-1] == x:
            stack.pop()
            answer += 2
        else:
            stack.append(x)
    
    return answer