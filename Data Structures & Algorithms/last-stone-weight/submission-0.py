class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        array = [-stone for stone in stones]
        heapq.heapify(array)

        while len(array) > 1:
            num1 = heapq.heappop(array)
            num2 = heapq.heappop(array)
            num3 = -(abs(num1 - num2))
            heapq.heappush(array, num3)

        return abs(array[0])