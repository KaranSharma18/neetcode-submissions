class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nums = heights
        n = len(nums)
        i, j = 0, n - 1
        area = 0
        
        while i < j:
            
            n1, n2 = nums[i], nums[j]
            l = min(n1, n2)
            area = max(area, (j - i) * l)
            
            if n1 < n2:
                i += 1
            else:
                j -= 1
                
        return area