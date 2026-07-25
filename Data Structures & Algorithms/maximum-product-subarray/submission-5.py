class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin, currmax = 1, 1
        res = nums[0]
        
        for num in nums:
            tmp = currmin * num
            currmin = min(num, num * currmin, num * currmax)
            currmax = max(num, num * currmax, tmp)
            res = max(res, currmax)
        
        return res
