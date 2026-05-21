class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = 0
        while l <= r:
            mid = (l + r)//2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/mid)
            if totalTime > h:
                l = mid + 1
            elif totalTime <= h:
                result = mid
                r = mid - 1
            else:
                break
        return result