class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_exist = set()
        l = dict()
        
        for num in nums:
            num_exist.add(num)
        
        max_length = 0
        for num in set(nums):
            j = num
            length = 0
            
            while j in num_exist:
                if j in l:
                    length = length + l[j]
                    break
                length += 1
                j += 1
            
            l[num] = length
            max_length = max(max_length, length)
        
        return max_length
        