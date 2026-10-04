class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        
        for n in seen:
            if n - 1 not in seen:
                length = 1
                
                while n + length in seen:
                    length += 1
                
                res = max(res, length)
        return res