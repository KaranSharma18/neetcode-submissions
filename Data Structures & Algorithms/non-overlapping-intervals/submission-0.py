class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        l1, r1 = intervals[0]
        count = 0
        
        for (l2, r2) in intervals[1:]:
            if l2 < r1:
                if r1 > r2:
                    l1, r1 = l2, r2
                count += 1
            else:
                l1, r1 = l2, r2
        
        return count
        