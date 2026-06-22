class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_exist = set()
        
        for num in nums:
            num_exist.add(num)
        
        length = 0
        for num in nums:
            j = num
            while j in num_exist:
                j += 1
            
            length = max(length, j - num)
        
        return length
        