class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        for _ in range(n):
            board.append(["."]*n)
        res = []
        def dfs(r):
            if r == n:
                copy = []
                for row in board:
                    copy.append("".join(row))
                res.append(copy)
                return
            for c in range(n):
                if self.placeQueen(r, c, board):
                    board[r][c] = "Q"
                    dfs(r+1)
                    board[r][c] = "."
                
        dfs(0)
        return res
    
    def placeQueen(self, r, c, board):
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
        
        row = r - 1
        column = c - 1
        while row >= 0 and column >= 0:
            if board[row][column] == "Q":
                return False
            row -= 1
            column -= 1
        
        row = r - 1
        column = c + 1
        while row >= 0 and column < len(board):
            if board[row][column] == "Q":
                return False
            row -= 1
            column += 1
        return True