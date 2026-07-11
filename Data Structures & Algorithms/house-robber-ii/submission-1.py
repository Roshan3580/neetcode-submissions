class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:len(nums)-1]), self.helper(nums[1:]))
    
    def helper(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for n in range(2, len(nums)):
            dp[n] = max(nums[n] + dp[n-2], dp[n-1])
        return dp[-1]