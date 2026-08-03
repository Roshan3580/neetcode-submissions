class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minH = [[grid[0][0], 0, 0]]
        visit = set()
        n = len(grid)
        visit.add((0,0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == n-1 and c == n - 1:
                return t
            for rowadd, coladd in [[1,0],[-1,0],[0,1],[0,-1]]:
                row, col = r + rowadd, c + coladd
                if (row >= n or col >= n or row < 0 or col < 0 
                or (row, col) in visit):
                    continue
                visit.add((row, col))
                heapq.heappush(minH, [max(t, grid[row][col]), row, col])
        