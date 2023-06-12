def solution(nums):
    ans = len(nums) // 2
    
    if ans >= len(set(nums)):
        ans = len(set(nums))
        
    return ans