class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_exist = set()
        l = dict()
        
        for num in nums:
            num_exist.add(num)
        
        max_length = 0
        for num in nums:
            j = num
            
            while j in num_exist:
                if j in l:
                    j += l[j]
                    length = j
                    break
                else:
                    j += 1
                print(num, j)
            
            l[num] = j - num
            max_length = max(max_length, j - num)
        
        return max_length