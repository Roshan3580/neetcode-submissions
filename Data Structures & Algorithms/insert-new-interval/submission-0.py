class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            a, b = min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])
            newInterval = [a,b]
            i += 1
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
            