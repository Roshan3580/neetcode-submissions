class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)

        def dfs(n):
            if n >= len(cost):
                return 0
            if cache[n] != -1:
                return cache[n]
            cache[n] = cost[n] + min(dfs(n+1), dfs(n+2))

            return cache[n]
        return min(dfs(0), dfs(1))