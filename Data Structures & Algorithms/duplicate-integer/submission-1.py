class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        
        for i in range(len(nums)):
            if nums[i] in hash_set:
                return True
            else:
                hash_set.add(nums[i])
        return False
        