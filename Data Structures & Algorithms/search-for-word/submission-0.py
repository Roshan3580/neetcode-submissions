class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        def dfs(row, column, i):
            if i == len(word):
                return True
            if (min(row, column) < 0 or row >= len(board) or 
            column >= len(board[0]) or (row, column) in seen or board[row][column] != word[i]):
                return False
            seen.add((row, column))
            res = (dfs(row+1, column, i+1) or dfs(row-1, column, i+1) 
            or dfs(row, column+1, i+1) or dfs(row, column-1, i+1))
            seen.remove((row,column))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False
