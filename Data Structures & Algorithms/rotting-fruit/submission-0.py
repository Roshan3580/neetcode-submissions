class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        def bfs(r, c):
            nonlocal fresh
            if (r < 0 or c < 0 or r >= row or c >= col
            or grid[r][c] != 1):
                return
            grid[r][c] = 2
            fresh -= 1
            q.append((r,c))
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r+1, c)
                bfs(r-1, c)
                bfs(r, c+1)
                bfs(r, c-1)
            time += 1
        return time if fresh == 0 else -1
                
