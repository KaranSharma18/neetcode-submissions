class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r, res = [1] * n, [1] * n, [1] * n
        
        l[0], r[-1] = nums[0], nums[-1]
        
        for i in range(1, n):
            j = n - i - 1
            l[i] = nums[i] * l[i - 1]
            r[j] = nums[j] * r[j + 1]
        
        for i in range(n):
            if i == 0: 
                res[i] = r[i + 1]
            elif i + 1 == n:
                res[i] = l[i - 1]
            else:
                res[i] = l[i - 1] * r[i + 1]
        
        return res