class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashset = set()
        
        for num in nums:
            hashset.add(num)
        res = 0
        
        for i in range(len(nums)):
            count = 1
            if nums[i] - 1 not in hashset:
                j = nums[i]
                while j + 1 in hashset:
                    count += 1
                    j += 1
                
                res = max(res, count)
                
        return res