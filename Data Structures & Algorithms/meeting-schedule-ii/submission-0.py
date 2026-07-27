"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x.start)
        rooms = []
        heapq.heappush(rooms, intervals[0].end)

        for i in range(1, len(intervals)):
            m = intervals[i]

            if m.start < rooms[0]:
                heapq.heappush(rooms, m.end)
            else:
                 heapq.heapreplace(rooms, m.end)

        return len(rooms)

        