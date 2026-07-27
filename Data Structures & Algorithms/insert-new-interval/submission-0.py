class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        st, end = newInterval
        
        for i, (l, r) in enumerate(intervals):
            if end < l:
                res.append([st, end])
                return res + intervals[i:]
            elif st > r:
                res.append([l, r])
            else:
                st, end = min(l, st), max(r, end)
                
        res.append([st, end])
        return res  