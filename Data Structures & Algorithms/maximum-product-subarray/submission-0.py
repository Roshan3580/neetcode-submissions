class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = 1
        minP = 1
        res = nums[0]
        for n in nums:
            tmp = maxP * n
            maxP = max(tmp, minP*n, n)
            minP = min(tmp, minP*n, n)
            res = max(res, maxP)
        return res