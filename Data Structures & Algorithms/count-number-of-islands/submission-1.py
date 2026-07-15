class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, column = len(grid), len(grid[0])
        islands = 0

        def dfs(x, y):
            if x < 0 or y < 0 or x >= row or y >= column or grid[x][y] == "0":
                return
            grid[x][y] = "0"
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x, y-1)
        
        for x in range(row):
            for y in range(column):
                if grid[x][y] == "1":
                    dfs(x, y)
                    islands += 1
        return islands