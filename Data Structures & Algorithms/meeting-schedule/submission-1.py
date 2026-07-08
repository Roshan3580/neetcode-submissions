"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        if intervals:
            prev = intervals[0].end
        else:
            return True
        for study in intervals[1:]:
            start, end = study.start, study.end
            if start < prev:
                return False
            else:
                prev = max(prev, end)
        return True