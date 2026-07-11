class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def dfs(n):
            if n >= len(nums):
                return 0
            if cache[n] != -1:
                return cache[n]
            cache[n] = max(dfs(n+2) + nums[n], dfs(n+3) + nums[n])
            return cache[n]
        return max(dfs(0), dfs(1))