class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def dfs(i):
            if cache[i] != -1:
                return cache[i]
            
            res = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    res = max(res, dfs(j) + 1)
            cache[i] = res
            return res
        
        return max(dfs(n) for n in range(len(nums)))