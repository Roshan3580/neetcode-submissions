class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        
        def bfs(row, col):
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or 
            grid[row][col] == -1 or (row, col) in visit):
                return
            visit.add((row, col))
            q.append((row, col))
            
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visit.add((row, col))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r+1, c)
                bfs(r-1, c)
                bfs(r, c+1)
                bfs(r, c-1)
            dist += 1
        