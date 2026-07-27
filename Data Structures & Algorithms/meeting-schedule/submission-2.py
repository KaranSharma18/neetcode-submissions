"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: (x.start, x.end))
        obj1 = intervals[0]
        l1, r1 = obj1.start, obj1.end

        for obj2 in intervals[1:]:
            l2, r2 = obj2.start, obj2.end
            if l2 < r1:
                return False
            l1, r1 = l2, r2
        return True

