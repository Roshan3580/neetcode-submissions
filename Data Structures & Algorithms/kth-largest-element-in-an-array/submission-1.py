class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        array = [-num for num in nums]
        heapq.heapify(array)

        while k > 1:
            heapq.heappop(array)
            k -= 1

        return -(array[0])