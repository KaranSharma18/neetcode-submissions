class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        
        for k in range(n - 2):
            i, j = k + 1, n - 1
            
            while i < j:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    i += 1
                    j -= 1
                    
                elif total < 0:
                  i += 1
                else:
                     j -= 1
                     
        return [list(t) for t in res] if res else []