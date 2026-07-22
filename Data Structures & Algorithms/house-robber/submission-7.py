class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        dp = {}
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        def dfs(i):
            if i < 0:
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = max(dfs(i - 2) + nums[i], dfs(i - 1))
            return dp[i]
        
        # print(dp)
        return dfs(n - 1)
        