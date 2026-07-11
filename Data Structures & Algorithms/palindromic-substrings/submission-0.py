class Solution:
    def countSubstrings(self, s: str) -> int:
        board = [[False] * len(s) for i in range(len(s))]
        count = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i<=2 or board[i+1][j-1]):
                    board[i][j] = True
                    count += 1
        return count