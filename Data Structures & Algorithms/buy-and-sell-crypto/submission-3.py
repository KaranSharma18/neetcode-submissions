class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = prices
        buy = 1000
        sell = 0
        profit = 0
        
        for i in range(len(nums)):
            if nums[i] < buy:
                buy = nums[i]
                continue
            
            profit = max(profit, nums[i] - buy)
        return profit