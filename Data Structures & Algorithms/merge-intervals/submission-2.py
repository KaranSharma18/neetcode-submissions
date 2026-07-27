class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        st, end = intervals[0]
        
        for i, (l, r) in enumerate(intervals[1:]):
            if end < l:
                res.append([st, end])
                st, end = l, r
            elif st > r:
                res.append([l, r])
            else:
                st, end = min(l, st), max(r, end)
                
        res.append([st, end])
        return res 
        