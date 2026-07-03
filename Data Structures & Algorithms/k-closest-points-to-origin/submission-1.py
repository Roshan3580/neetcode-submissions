class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = [[] for i in range(k)]
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (dist, (x, y)))
        
        for i in range(k):
            res[i] = heapq.heappop(heap)[1]
        return res