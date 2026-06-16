class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = {}
        
        for num in nums:
            if exists.get(num, False):
                return True
            else:
                exists[num] = True
        
        return False