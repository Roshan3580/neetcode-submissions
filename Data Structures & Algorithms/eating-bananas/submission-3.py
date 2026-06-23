class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r
        while l <= r:
            mid = l + (r-l)//2
            time = 0
            for n in piles:
                time += math.ceil(n/mid)
            if time <= h:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result