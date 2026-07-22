class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
            
        dp = [-1] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1]) 
        
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        # print(dp)
        return dp[-1]
        