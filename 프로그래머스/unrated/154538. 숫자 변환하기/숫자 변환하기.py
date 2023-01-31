from collections import deque

INF = int(1e9)

def solution(x, y, n):
    dp = [INF] * 1000001
    q = deque()
    q.append(x)
    dp[x] = 0
    
    while q:
        cx = q.popleft()
        if cx == y:
            break
        
        for nx in [cx + n, cx * 2, cx * 3]:
            if 1 <= nx <= y and dp[nx] == INF:
                dp[nx] = min(dp[cx] + 1, dp[nx])
                q.append(nx)
                
    return dp[y] if dp[y] != INF else -1