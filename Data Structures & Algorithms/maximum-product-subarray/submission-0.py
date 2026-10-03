class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        res = dp[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] * nums[i])
            res = max(res, dp[i])
        print(dp)
        return res