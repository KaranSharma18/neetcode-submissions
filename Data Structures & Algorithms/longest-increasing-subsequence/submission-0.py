class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {} 
        res = 0
        
        def dfs(prev, i):
            if (prev, i) in memo:
                return memo[(prev, i)]
                
            if i == n:
                return 0
            
            best = dfs(prev, i + 1)
            
            if nums[prev] < nums[i]:
                best = max(best, 1 + dfs(i, i + 1))
            
            memo[(prev, i)] = best
            return memo[(prev, i)]
        
        for i in range(n):
            res = max(1 + dfs(i, i + 1), res)
        return res
        