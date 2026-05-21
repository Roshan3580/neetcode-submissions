class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.array = nums
        self.k = k
        heapq.heapify(self.array)
        while len(self.array) > k:
            heapq.heappop(self.array)

    def add(self, val: int) -> int:
        heapq.heappush(self.array, val)
        if len(self.array) > self.k:
            heapq.heappop(self.array)
        return self.array[0]
