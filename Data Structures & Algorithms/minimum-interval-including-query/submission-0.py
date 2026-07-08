class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries
        output = {}
        minHeap = []
        i = 0
        res = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minHeap, ((intervals[i][1]-intervals[i][0]+1), intervals[i][1]))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            if minHeap:
                output[q] = minHeap[0][0]
            else:
                output[q] = -1
        for q in queries:
            res.append(output[q])
        return res