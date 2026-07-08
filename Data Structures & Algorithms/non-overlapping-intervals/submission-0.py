class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start <  prev:
                prev = min(end, prev)
                res += 1
            else:
                prev = end
        return res