class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        l, w = 0, 0
        area, res = 0, 0
        
        
        while i < j:
            p1 = heights[i]
            p2 = heights[j]
            
            l = min(p1, p2)
            w = j - i
            area = l * w
            res = max(area, res)
            if p1 < p2:
                i += 1
            else:
                j -= 1
                
        return res
        