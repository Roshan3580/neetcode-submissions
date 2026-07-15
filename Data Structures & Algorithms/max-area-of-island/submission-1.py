class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = float('-inf')
        row, column = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= row or y >= column or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
             
            return 1 + (dfs(x+1, y) + dfs(x, y+1) + dfs(x-1, y) + dfs(x, y-1))
        
        for x in range(row):
            for y in range(column):
                max_size = max(max_size, dfs(x, y))
        return max_size
