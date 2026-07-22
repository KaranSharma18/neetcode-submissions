class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        if m == 1:
            return nums[0]
            
        def rob_linear(arr):
            n = len(arr)
            if n == 1:
                return arr[0]
                
            dp = {}
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            
            def dfs(i):
                if i < 0:
                    return 0
                if i in dp:
                    return dp[i]
                
                dp[i] = max(dfs(i - 2) + arr[i], dfs(i - 1))
                return dp[i]
            
            return dfs(n - 1)
            
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
        