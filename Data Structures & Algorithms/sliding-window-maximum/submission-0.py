class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for l in range(len(nums) - k + 1):
            temp = nums[l:l+k]
            print(temp)
            result.append(max(temp))

        return result