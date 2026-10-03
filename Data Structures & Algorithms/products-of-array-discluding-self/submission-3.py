class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r, res = [1] * n, [1] * n, [1] * n
        
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]
        
        for j in range(n - 2, -1, -1):
            r[j] = r[j + 1] * nums[j + 1]
        
        for i in range(n):
            res[i] = l[i] * r[i]
        
        return res