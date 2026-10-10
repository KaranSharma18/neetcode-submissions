class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        res = 0

        while i < j:
            h = min(heights[i], heights[j])
            res = max(res, (j - i) * h)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return res