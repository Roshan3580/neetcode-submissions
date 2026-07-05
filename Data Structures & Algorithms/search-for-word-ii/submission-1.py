class TrieNode:
    def __init__(self):
        self.end = False
        self.child = {}

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        rows, columns = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if ((r,c) in visit or r < 0 or c < 0 or r >= rows or c >= columns 
            or board[r][c] not in node.child):
                return

            visit.add((r,c))
            node = node.child[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r,c))

        for r in range(rows):
            for c in range(columns):
                dfs(r,c,root,"")
        return list(res)
            