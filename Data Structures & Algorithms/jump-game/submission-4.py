class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n == 1:
            return True
            
        i, j = n - 2, n - 1
        while i >= 0:
            if nums[i] >= j - i:
                j = i
            i -= 1
        
        return j == 0
        