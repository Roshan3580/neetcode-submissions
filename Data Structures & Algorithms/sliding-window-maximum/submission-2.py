class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l = 0
        r = l + k - 1
        while r < len(nums):
            result.append(max(nums[l:r+1]))
            l += 1
            r += 1
        return result