class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [[0] * (n+1) for _ in range(n+1)]

        for i in range(len(nums)-1, -1, -1):
            for j in range(i - 1, -2, -1):
                res = cache[i+1][j+1]
                if j == -1 or nums[j] < nums[i]:
                    res = max(res, 1 + cache[i+1][i+1])
                
                cache[i][j+1] = res

        return cache[0][0]